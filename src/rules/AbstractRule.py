from abc import ABC, abstractmethod


class TrafficRule(ABC):

    @abstractmethod
    def apply(data_object, ip_score):
        pass


