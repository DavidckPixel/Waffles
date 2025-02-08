from .AbstractRule import TrafficRule
from RuleConfig import UserAgentSwitchRuleConfig as rule


class UserAgentSwitch(TrafficRule):

    def apply(self, data_object):

        attack_dict = dict()

        data_object.create_attack_groups(attack_dict, 5)
        for (ip, attacks) in attack_dict.items():
            count = 0
            for attack in attacks:
                if not all(x == attack[0] for x in attack):
                    count += 1

            if count > 1 or len(attacks) == 1:
                rl = rule['UsSwitch1']
                data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])
            elif count == 0:
                rl = rule['UsSwitch2']
                data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])

