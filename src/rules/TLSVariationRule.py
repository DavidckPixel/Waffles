from .AbstractRule import TrafficRule
from ..Generic import count_property_values
from RuleConfig import TLSVariationRuleConfig as rule


class TLSVariationRule(TrafficRule):

    def apply(self, data_object):
        for (ip, entries) in data_object.ip_dict.items():

            tls = count_property_values(entries, 'clientSSLProtocol')

            if (len(tls) > 2):
                rl = rule['TLS1']
                data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])
            elif (len(tls) > 1):
                if 'none' in tls and 'TLSv1.2' in tls:
                    self.tls_usage_are_redirect(tls['TLSv1.2'], tls['none'], data_object.ip_score[ip])
                elif 'none' in tls and 'TLSv1.3' in tls:
                    self.tls_usage_are_redirect(tls['TLSv1.3'], tls['none'], data_object.ip_score[ip])
                else:
                    rl = rule['TLS4']
                    data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])
            else:
                if 'TLSv1.2' in tls or 'TLSv1.3' in tls:
                    rl = rule['TLS5']
                    data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])
                else:
                    rl = rule['TLS6']
                    data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])

    def tls_usage_are_redirect(self, tls, none, data):
        diff = tls / none
        if 0.5 <= diff <= 2:
            rl = rule['TLS2']
            data.apply_rule(rl['description'], rl['actions'])
        else:
            rl = rule['TLS3']
            data.apply_rule(rl['description'], rl['actions'])

