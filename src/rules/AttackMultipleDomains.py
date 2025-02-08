from .AbstractRule import TrafficRule
from ..filters import filter_attack_multiple_domains
from RuleConfig import AttackMultiDomainConfig as rule


class AttackMultiDomain(TrafficRule):
    def apply(self, data_object):
        filtered_ip_dict = filter_attack_multiple_domains(data_object)
        for ip in filtered_ip_dict.keys():
            rl = rule['MultiDom1']
            data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])
