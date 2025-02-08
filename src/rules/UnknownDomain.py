from .AbstractRule import TrafficRule
import config
from RuleConfig import UnknownDomainRuleConfig as rule


class UnknownDomain(TrafficRule):
    def apply(self, data_object):
        for (ip, entries) in data_object.ip_dict.items():
            for entry in entries:
                if entry.clientRequestHTTPHost not in config.domains:
                    rl = rule['Unkn1']
                    data_object.ip_score[entry.clientIP].apply_rule(rl['description'], rl['actions'])
                    break
