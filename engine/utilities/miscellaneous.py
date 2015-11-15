# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% PERCENTAGE COMPLETION FUNCTIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
import json
from engine.utilities.constants import *

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
    necessary_keys = [CREATED_AT, ENTITIES, TEXT, RETWEET_COUNT, ID, USER, COORDINATES, PLACE]
    try:
        keys = json.loads(obj).keys()
        for key in necessary_keys:
            if key not in keys:
                return False
    except:
        return False
    return True


