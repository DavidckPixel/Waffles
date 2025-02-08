from config import group_time
from datetime import datetime
from .TrafficScore import TrafficScore


class TrafficDataStructure:


    def __init__(self, traffic_list):
        self.traffic_list = traffic_list
        self.ip_dict = dict()
        self.asn_dict = dict()
        self.attack_dict = dict()

        self.create_dict('clientIP', self.ip_dict)
        self.create_dict('clientAsn', self.asn_dict)
        self.create_attack_groups(self.attack_dict, group_time)
        self.ip_score = dict()

        for ip in self.ip_dict.keys():
            self.ip_score[ip] = TrafficScore()


    def create_dict(self, prop, dic):
        for entry in self.traffic_list:
            data = vars(entry)[prop]
            if data in dic:
                dic[data].append(entry)
            else:
                dic[data] = [entry]


    def create_attack_groups(self, dic, n):
        for (ip, entry_list) in self.ip_dict.items():

            entry_list.sort(key=lambda t: t.datetime, reverse=False)

            attacks = []

            last = entry_list[0]
            attack = [last]

            for entry in entry_list[1:]:
                diff = (entry.datetime - last.datetime).total_seconds()

                if diff > n:
                    attacks.append(attack)
                    attack = [entry]
                else:
                    attack.append(entry)
                last = entry

            attacks.append(attack)
            dic[ip] = attacks



