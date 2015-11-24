from bson.code import Code
from utilities.mongo import *
from utilities.os_util import *
from utilities.time_management import *
from utilities.constants import *
from pymongo import MongoClient


ROOT = get_dir(__file__)

TODAY = get_today()
NEW_WEEK_START = get_week_start(TODAY)
OLD_WEEK_START = get_prev_day(NEW_WEEK_START)


PREVIOUS_WEEKLY_COLLECTION_NAME = WEEKLY_RESULTS_COLLECTION + get_date_string(OLD_WEEK_START)
NEW_WEEKLY_COLLECTION_NAME = WEEKLY_RESULTS_COLLECTION + get_date_string(NEW_WEEK_START)
LATEST_RESULTS_COLLECTION_NAME = RESULTS_COLLECTION + get_date_string(TODAY)
OLDEST_RESULTS_COLLECTION_NAME = RESULTS_COLLECTION + get_date_string(OLD_WEEK_START)


create_result(TWEETS_DB, PREVIOUS_WEEKLY_COLLECTION_NAME)
create_result(TWEETS_DB, LATEST_RESULTS_COLLECTION_NAME)
create_result(TWEETS_DB, OLDEST_RESULTS_COLLECTION_NAME)


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
    client.close()
    stop()
