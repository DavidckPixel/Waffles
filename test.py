import subprocess
from src.label import LabelAlgorithm
import os
import psutil
from main import print_logo

def test_get_blocked_traffic():
    print("We will test the API-script for getting all blocked traffic")

    zone_id = input("What is the Zone_ID from where we will read the blocked traffic?")
    start_date = input("What is the start-date? (format yyyy-mm-dd)")
    end_date = input("What is the end-date? (max 72 hours) (format yyyy-mm-dd)")

    api_key = input("Please input your API-key")

    print("Running Script, please stand by")
    params = (zone_id, start_date + 'T00:00:00Z', end_date + 'T23:59:59Z', api_key)

    subprocess.check_call("ApiScripts/GetBlockedTraffic.sh '%s' '%s' '%s' '%s'" % params, shell=True)


def test_get_ip_traffic():
    print("We will test the API-script for getting entries of a single IP")

    zone_id = input("What is the Zone_ID from where we will read the blocked traffic?")
    start_date = input("What is the start-date? (format yyyy-mm-dd)")
    end_date = input("What is the end-date? (max 72 hours) (format yyyy-mm-dd)")

    api_key = input("Please input your API-key")
    ip = input("What IP do you want to get?")

    print("Running script to get all entries")
    params = (ip, zone_id, 'N', api_key, start_date + 'T00:00:00Z', end_date + 'T23:59:59Z', 'all')
    call = "ApiScripts/GetTrafficOfIP.sh '%s' '%s' '%s' '%s' '%s' '%s' '%s'"

    subprocess.check_call(call % params, shell=True)

    print("Running script to get non-blocked entries")
    params2 = (ip, zone_id, 'L', api_key, start_date + 'T00:00:00Z', end_date + 'T23:59:59Z', 'passed') 

    subprocess.check_call(call % params2, shell=True)




# inner psutil function
def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss

# decorator function
def profile(func):
    def wrapper(*args, **kwargs):

        mem_before = process_memory()
        result = func(*args, **kwargs)
        mem_after = process_memory()
        print("{}:consumed memory: {:,}".format(
            func.__name__,
            mem_before, mem_after, mem_after - mem_before))

        return result
    return wrapper


print_logo()

@profile

def test_rule():
    lb = LabelAlgorithm()
    lb.apply_rules()

    ips = lb.analyse_ip_score()

    for (ip, x) in ips.items():
        if x.thread_level > -1:
            print("IP: {0} -- {1}".format(ip, x))
            for r in x.applied_rules:
                print(r)
            print('------------------')

test_rule()
