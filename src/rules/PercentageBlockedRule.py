from .AbstractRule import TrafficRule
from RuleConfig import PercentageBlockedRuleConfig as rule

class PercentageBlockedRule(TrafficRule):

    def apply(self, data_object):

        for (ip, entries) in data_object.ip_dict.items():
            allowed = sum(e.securityAction == 'unknown' for e in entries)
            blocked = len(entries) - allowed

            diff = allowed / blocked

            if 0.5 <= diff <= 10:
                rl = rule['PerBl1']
                data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])
            elif diff < 0.5:
                rl = rule['PerBl2']
                data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])
            else:
                rl = rule['PerBl3']
                data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])

            if (blocked == 1 and allowed == 0):
                rl = rule['PerBl4']
                data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])
