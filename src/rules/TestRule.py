from .AbstractRule import TrafficRule


class TestRule(TrafficRule):

    def apply(self, data_object):
        for entry in data_object.traffic_list:
            entry.traffic_score.thread_level += 50
