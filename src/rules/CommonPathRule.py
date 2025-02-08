from .AbstractRule import TrafficRule
from RuleConfig import CommonPathRuleConfig as rule

class CommonPathRule(TrafficRule):
    def apply(self, data_object):
        path_index = self.count_different_paths(data_object.ip_dict)

        for (ip, entries) in data_object.ip_dict.items():
            score = sum(path_index[e.clientRequestPath] for e in entries if not e.clientRequestPath == '/') / len(entries)

            if score < 3 and len(entries) > 2:
                rl = rule['CommPath2']
            else:
                rl = rule['CommPath1']
            data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])

    def count_different_paths(self,ip_dict):
        new_dict = dict()

        for (ip, entries) in ip_dict.items():
            ip_paths = set([e.clientRequestPath for e in entries])
            for path in ip_paths:
                if path in new_dict:
                    new_dict[path] += 1
                else:
                    new_dict[path] = 1

        return new_dict



