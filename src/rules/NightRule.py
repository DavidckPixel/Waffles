from .AbstractRule import TrafficRule
from RuleConfig import NightRuleConfig as rule
import numpy as np

# Timeshift list from CET
time_shift = {"CH": 0,
              "IN": -5,
              "BD": -5,
              "KH": -6,
              "UY": 4,
              "KR": -8,
              "MA": 0,
              "IS": 1,
              "BR": 4,
              "CL": 4,
              "AU": -9,
              "DK": 0,
              "LT": -1,
              "HR": 0,
              "MD": -1,
              "AT": 0,
              "ID": -7,
              "HK": -7,
              "NO": 0,
              "BA": 0,
              "JP": -8,
              "RO": -1,
              "ES": 0,
              "FI": -1,
              "CA": -5,
              "NZ": -12,
              "HU": 0,
              "CN": -7,
              "BE": 0,
              "UA": -1,
              "PL": 0,
              "EG": -1,
              "SE": 0,
              "GB": 1,
              "DE": 0,
              "IE": 1,
              "RU": -2,
              "BG": -1,
              "AZ": -3,
              "FR": 0,
              "NL": 0,
              "SG": -7,
              "US": 7}


class NightRule(TrafficRule):

    def apply(self, data_object):

        for (ip, attacks) in data_object.attack_dict.items():
            country = attacks[0][0].clientCountryName
            night = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

            if country in time_shift:
                shift = time_shift[country] * 1
                night = night[shift:] + night[:shift]


            night_list = [all(night[i.datetime.hour] == 1 for i in attack) for attack in attacks]
            if all(night_list):
                rl = rule['Night1']
                data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])
            elif (not any(night_list)) and len(data_object.ip_dict[ip]) > 3:
                rl = rule['Night2']
                data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])
            else:
                rl = rule['Night3']
                data_object.ip_score[ip].apply_rule(rl['description'], rl['actions'])


