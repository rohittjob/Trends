# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% PERCENTAGE COMPLETION FUNCTIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
import json


def check_percent(cur_count, total_count, interval, prev):      # interval it is the interval of display,
                                                                # prev is previously displayed percentage
    if total_count == 0:
        return 0
    per = (cur_count * 100) / total_count
    rounded_per = (per/interval)*interval
    while prev < rounded_per:
        prev += interval
    print '\r',
    print str(prev) + '% complete',
    return prev


def is_json(obj):
    try:
        boolean = (len(json.loads(obj).keys()) > 0)
    except:
        return False
    return boolean


