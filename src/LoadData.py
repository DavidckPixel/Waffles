from os import listdir
from os.path import isfile, join
import json
from .Traffic import Traffic
from .DataStructure import TrafficDataStructure

path = 'logs'


def load_log_files():
    log_files = [join(path, f) for f in listdir(path) if isfile(join(path, f))]

    traffic_list = []

    for file in log_files:
        traffic_list += load_log_file(file)

    return TrafficDataStructure(traffic_list)


def load_log_file(file):
    traffic_list = []

    with open(file) as json_data:
        data = json.load(json_data)

    entries = data['data']['viewer']['zones'][0]['httpRequestsAdaptive']
    for entry in entries:
        traffic_list.append(Traffic(**entry))

    # Error Checking here!

    return traffic_list
