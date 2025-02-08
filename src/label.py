from .LoadData import load_log_files
from .rules import NightRule, AttackMultipleDomains, UnknownDomain, Redirected, Alphabetical, TimeRule, UserAgentSwitch, CommonPathRule, HTTPVersionRule, TLSVariationRule, AttacksApexRule, AverageTimeRule, MultiDayRule, PercentageBlockedRule, MultiIPAsn, OperCountryRule, ExpectedBrowserRule


class LabelAlgorithm:
    def __init__(self):
        self.ds = load_log_files()

    rules = [NightRule.NightRule(),
             AttackMultipleDomains.AttackMultiDomain(),
             UnknownDomain.UnknownDomain(),
             Redirected.Redirected(),
             Alphabetical.Alphabetical(),
             UserAgentSwitch.UserAgentSwitch(),
             TimeRule.TimeRule(),
             CommonPathRule.CommonPathRule(),
             HTTPVersionRule.HTTPVersionRule(),
             TLSVariationRule.TLSVariationRule(),
             AttacksApexRule.AttacksApexRule(),
             AverageTimeRule.AverageTimeRule(),
             MultiDayRule.MultiDayRule(),
             PercentageBlockedRule.PercentageBlockedRule(),
             MultiIPAsn.MultiIPAsn(),
             OperCountryRule.OperCountryRule(),
             ExpectedBrowserRule.ExpectedBrowserRule()
             ]

    # rules = [MultiDayRule.MultiDayRule()]

    def apply_rules(self):
        print(len(self.ds.ip_dict))
        for rule in self.rules:
            rule.apply(self.ds)

    def analyse_ip_score(self):
        relevant_scores = dict()

        for (ip, score) in self.ds.ip_score.items():

            if score.human_factor > 0.3 and score.bot_factor < 2:
                score.apply_rule('Human Factor is above 0.3', [{"value": 0.3, "target": 'thread_level'}])

        for (ip, score) in self.ds.ip_score.items():
            if score.thread_level > 1:
                relevant_scores[ip] = score
            elif score.human_factor > 0.5 and score.bot_factor < 3:
                relevant_scores[ip] = score

        return relevant_scores


