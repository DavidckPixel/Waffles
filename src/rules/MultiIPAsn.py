from .AbstractRule import TrafficRule
from RuleConfig import MultiIPAsnConfig as rule
from ..Generic import count_property_values


class MultiIPAsn(TrafficRule):

    def apply(self, data_object):

        for (asn, entries) in data_object.asn_dict.items():

            ips = count_property_values(entries, 'clientIP')

            if len(ips) > 1:
                for ip in ips.keys():
                    rl = rule["MuAsn"]
                    data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])
