from .AbstractRule import TrafficRule
from RuleConfig import HTTPVersionRuleConfig as rule


class HTTPVersionRule(TrafficRule):

    def apply(self, data_object):
        for (ip, entries) in data_object.ip_dict.items():

            http = self.get_http_used(entries)
            if http['HTTP/1.1'] > 0:
                a = len({k: v for (k, v) in http.items() if v > 0})
                if a > 2:
                    rl = rule['HTTPVer1']
                    data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])
                elif a > 1:
                    rl = rule['HTTPVer2']
                    data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])
                else:
                    rl = rule['HTTPVer3']
                    data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])
            if http['HTTP/3'] > 0:
                rl = rule['HTTPVer4']
                data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])

    def get_http_used(self, entries):
        http = {'HTTP/1.0': 0, 'HTTP/1.1': 0, 'HTTP/2': 0, 'HTTP/3': 0}

        for entry in entries:
            http[entry.clientRequestHTTPProtocol] += 1

        return http 
