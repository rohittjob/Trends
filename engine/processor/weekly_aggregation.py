from bson.code import Code
from engine.utilities.time_management import *
from engine.utilities.os_util import *
from engine.utilities.mongo import *
from engine.utilities.constants import *
from pymongo import MongoClient
from os.path import join

ROOT = get_dir(__file__)

TODAY = get_today()
WEEK_START = TODAY - timedelta(days=7)
NEW_WEEK_START = WEEK_START + timedelta(days=1)


PREVIOUS_WEEKLY_COLLECTION_NAME = WEEKLY_RESULTS_COLLECTION + get_date_string(WEEK_START)
NEW_WEEKLY_COLLECTION_NAME = WEEKLY_RESULTS_COLLECTION + get_date_string(NEW_WEEK_START)
LATEST_RESULTS_COLLECTION_NAME = RESULTS_COLLECTION + get_date_string(TODAY)
OLDEST_RESULTS_COLLECTION_NAME = RESULTS_COLLECTION + get_date_string(WEEK_START)


create_result(PREVIOUS_WEEKLY_COLLECTION_NAME)
create_result(LATEST_RESULTS_COLLECTION_NAME)
create_result(OLDEST_RESULTS_COLLECTION_NAME)


client = MongoClient()
db = client.tweets

previous_week_collection = db[PREVIOUS_WEEKLY_COLLECTION_NAME]
latest_result_collection = db[LATEST_RESULTS_COLLECTION_NAME]
oldest_result_collection = db[OLDEST_RESULTS_COLLECTION_NAME]


if __name__ == '__main__':

    print 'Started Weekly Aggregation... ',

    start()

    map_add_function = Code(open(join(ROOT, AGGREGATION_MAP_ADD_FUNCTION), 'r').read())
    map_subtract_function = Code(open(join(ROOT, AGGREGATION_MAP_SUBTRACT_FUNCTION), 'r').read())
    reduce_function = Code(open(join(ROOT, AGGREGATION_REDUCE_FUNCTION), 'r').read())

    previous_week_collection.map_reduce(map_add_function, reduce_function, NEW_WEEKLY_COLLECTION_NAME)
    latest_result_collection.map_reduce(map_add_function, reduce_function, {'reduce': NEW_WEEKLY_COLLECTION_NAME})
    oldest_result_collection.map_reduce(map_subtract_function, reduce_function, {'reduce': NEW_WEEKLY_COLLECTION_NAME})

    print 'Finished'
    stop()
