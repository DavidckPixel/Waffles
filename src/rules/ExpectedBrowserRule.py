from .AbstractRule import TrafficRule
from config import common_browser
from RuleConfig import ExpectedBrowserRule as rule

class ExpectedBrowserRule(TrafficRule):

    def apply(self, data_object):

        def check_browser_in_string(agent):
            return any(x in agent for x in common_browser)

        for (ip, entries) in data_object.ip_dict.items():
            browser = [check_browser_in_string(a.userAgent) for a in entries]
            if all(browser):
                rl = rule['ExpBr1']
                data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])
            elif not any(browser):
                rl = rule['ExpBr2']
                data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])

