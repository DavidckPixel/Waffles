from .AbstractRule import TrafficRule
from RuleConfig import MultiDayRuleConfig as rule

class MultiDayRule(TrafficRule):

    def apply(self, data_object):
        day_attacks = dict()

        seconds = 43200
        data_object.create_attack_groups(day_attacks, seconds)

        for (ip, attacks) in day_attacks.items():
            if len(attacks) == 1:
                continue

            rl = rule['MuDay1']
            data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])


