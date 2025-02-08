from .AbstractRule import TrafficRule
from config import operational_countries
from RuleConfig import OperCountryRuleConfig as rule


class OperCountryRule(TrafficRule):

    def apply(self, data_object):

        for (ip, entries) in data_object.ip_dict.items():
            if entries[0].clientCountryName in operational_countries:
                rl = rule['OpCo']
                data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])



