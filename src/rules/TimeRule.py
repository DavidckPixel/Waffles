from .AbstractRule import TrafficRule
from RuleConfig import TimeRuleConfig as rule

class TimeRule(TrafficRule):

    def apply(self, data_object):

        attack_dict = dict()

        data_object.create_attack_groups(attack_dict, 1)
        for (ip, attacks) in attack_dict.items():
            time_count = 0
            for attack in attacks:
                if len(attack) > 2:
                    time_count += 1

            if time_count > len(attacks) - 2:
                rl = rule['Time1']
                data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])


