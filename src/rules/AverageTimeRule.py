from .AbstractRule import TrafficRule
from statistics import mean
from RuleConfig import AverageTimeRuleConfig as rule

class AverageTimeRule(TrafficRule):

    def apply(self, data_object):

        def time_diff(t1, t2):
            return (t2.datetime - t1.datetime).total_seconds()

        for (ip, entries) in data_object.ip_dict.items():
            if len(entries) == 1:
                continue

            average = mean(time_diff(t1, t2) for (t1, t2) in zip(entries, entries[1:]))

            if (average < 1):
                rl = rule['AvTime1']
                data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])
            elif average < 10:
                rl = rule['AvTime2']
                data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])
            elif average > 1000:
                rl = rule['AvTime3']
                data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])
            elif average > 10000:
                rl = rule['AvTime4']
                data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])



