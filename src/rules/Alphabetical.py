from .AbstractRule import TrafficRule
from RuleConfig import AlphabeticalRuleConfig as rule
from ..filters import filter_attack_multiple_domains
from ..Generic import create_dict_of_entries


class Alphabetical(TrafficRule):

    def apply(self, data_object):
        filtered_ip_dict = filter_attack_multiple_domains(data_object,True)

        for (ip, entries) in filtered_ip_dict.items():
            count_path = self.apply_alphabetical_on_property('clientRequestPath', entries)
            count_query = self.apply_alphabetical_on_property('clientRequestQuery', entries)

            if count_path + count_query > 0:
                rl = rule['AlphRule1']
                data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])

    def apply_alphabetical_on_property(self, prop, entries):

        path_dict = create_dict_of_entries(entries, prop)
        count = 0

        for (path, path_entries) in path_dict.items():

            # Add this to config file
            path_entries = [p for p in path_entries if p.clientRequestHTTPHost.split('.')[1] == 'apex.domain']
            if len(set([t.clientRequestHTTPHost for t in path_entries])) < 3:
                continue

            sorted_entries = sorted(path_entries, key=lambda e: e.datetime)

            is_sorted = [sorted_entries[i].clientRequestHTTPHost <= sorted_entries[i+1].clientRequestHTTPHost for i in range(len(sorted_entries) - 1)]

            if all(is_sorted):
                count += 1
            elif sorted_entries[0].clientRequestHTTPHost[0] == 'w' and all(is_sorted[1:]):
                count += 1

        return count
