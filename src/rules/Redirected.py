from .AbstractRule import TrafficRule
import config
from RuleConfig import RedirectedRuleConfig as rule

class Redirected(TrafficRule):

    rule = "HTTP request was redirected"

    def apply(self, data_object):
        for (ip, attacks) in data_object.attack_dict.items():
            all_redirected = []

            for attack in attacks:
                index = 0
                max_index = len(attack)

                for entry in attack:

                    skip = False
                    domain = entry.clientRequestHTTPHost
                    if domain not in config.redirect.keys():
                        index += 1
                        continue
                    n = index + 1
                    while n < max_index and (attack[n].datetime - entry.datetime).total_seconds() <= 1:
                        redirected_to = config.redirect[domain]

                        if redirected_to == attack[n].clientRequestHTTPHost and domain == attack[n].clientRefererHost:
                            entry.traffic_score.set_flag(self.rule, True, 'redirected')
                            all_redirected.append(True)
                            skip = True
                            break
                        n += 1

                    if not skip:
                        all_redirected.append(False)
                    index += 1

            if not all_redirected:
                continue

            score = data_object.ip_score[ip]
            if all(all_redirected):
                rl = rule['Redir1']
                score.apply_rule(rl['description'], rl['actions'])
            elif not any(all_redirected):
                rl = rule['Redir2']
                score.apply_rule(rl['description'], rl['actions'])
            else:
                rl = rule['Redir3']
                score.apply_rule(rl['description'], rl['actions'])
