from .AbstractRule import TrafficRule
from RuleConfig import AttacksApexRuleConfig as rule

class AttacksApexRule(TrafficRule):

    def apply(self, data_object):

        for (ip, entries) in data_object.ip_dict.items():

            apex1 = 0
            apex2 = 0

            for entry in entries:

                # Add this too config
                if 'apexdomain' in entry.clientRequestHTTPHost:
                    apex2 += 1
                else:
                    apex1 += 1

            if apex2 == 0:
                rl = rule['AtApex2']
                data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])
                pass
            elif apex1 == 0:
                rl = rule['AtApex1']
                data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])
            elif apex1 > apex2:
                rl = rule['AtApex3']
                data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])
            elif apex2 > apex1:
                rl = rule['AtApex4']
                data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])

