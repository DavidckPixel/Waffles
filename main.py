from datetime import datetime, timedelta
import subprocess
import config
import time
import json
import sys
import argparse
from os.path import isfile, join
from os import listdir
from src.label import LabelAlgorithm


log_file = ""
parser = argparse.ArgumentParser()
parser.add_argument('-g', '--get', action='store_true', help="Get the weeks data from the API first")


def main():

    print_logo()
    args = parser.parse_args()

    if args.get:
        get_week_data()

    lb = LabelAlgorithm()
    lb.apply_rules()

    ips = lb.analyse_ip_score()

    for (ip, x) in ips.items():
        if x.thread_level > -1:
            print("IP: {0} -- {1}".format(ip, x))
            for r in x.applied_rules:
                print(r)
            print('------------------')


def get_week_data():
    zones = config.zones
    api = input("Input API-key ")
    current_date = datetime.today()

    for x in range(7):
        for zone in zones:
            get_date = current_date - timedelta(days=x)
            get_blocked_traffic_from_api(get_date.strftime('%Y-%m-%d'), api, zone)

    ips = get_list_of_blocked_ips()

    for zone in zones:
        get_ip_list_traffic_from_api(api, zone, ips, current_date)


def get_blocked_traffic_from_api(date, api, zone):
    params = (zone["zone_id"], date + 'T00:00:00Z', date + 'T23:59:59Z', api, zone["name"])
    call = 'ApiScripts/GetBlockedTraffic.sh' + ' %s' * len(params)

    print("Getting data for zone: {0} on day {1}".format(zone['zone_id'], date))

    subprocess.check_call(call % params, shell=True)
    time.sleep(5)


def get_ip_list_traffic_from_api(api, zone, ips, current_date):
    print("-----Getting Traffic - Zone: {0}".format(zone["zone_id"]))
    c = 0
    for ip in ips:
        get_ip_traffic_from_api(api, zone, ip, current_date)
        c += 1
        if c % 10 == 0:
            perc = (c / len(ips)) * 100
            print("Process: {0}".format(perc))


def get_ip_traffic_from_api(api, zone, ip, current_date):
    begin_date = current_date - timedelta(days=7)
    params = (ip,
              zone["zone_id"],
              'L',
              api,
              begin_date.strftime('%Y-%m-%d') + 'T00:00:00Z',
              current_date.strftime('%Y-%m-%d') + 'T23:59:59Z',
              zone["name"] + '-' + ip.replace('.', '-'))

    call = 'ApiScripts/GetTrafficOfIP.sh' + ' %s' * len(params)
    subprocess.check_call(call % params, shell=True)
    time.sleep(5)


def get_list_of_blocked_ips():
    path = 'logs'
    logs = [join(path, f) for f in listdir(path) if isfile(join(path, f)) and 'log_blocked' in f]

    ips = []

    for log in logs:
        with open(log) as json_data:
            data = json.load(json_data)

        entries = data['data']['viewer']['zones'][0]['httpRequestsAdaptive']
        for entry in entries:
            ips.append(entry['clientIP'])

    return set(ips)


def analyse_ip_score(data_object):
    relevant_scores = dict()

    for (ip, score) in data_object.ip_score.items():
        if score.human_factor > 0.3 and score.bot_factor < 2:
            score.apply_rule('Human Factor is above 0.3', {'target': 'thread_level','value': 0.3})

    for (ip, score) in data_object.ip_score.items():
        if score.thread_level > 1:
            relevant_scores[ip] = score
        elif score.human_factor > 0.5:
            relevant_scores[ip] = score

    return relevant_scores


def print_logo():
    for line in open('logo.txt'):
        print(line.replace('\n', ''))


if __name__ == '__main__':
    main()
