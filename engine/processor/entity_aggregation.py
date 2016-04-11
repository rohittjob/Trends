'''

 Refer reference_files/daily_aggregation.py
 Does the exact same thing. But the names of collections might be different.
 Finds the count of each entity frequently, merging into a single results file.

'''
from os.path import join
from bson.code import Code
from pymongo import MongoClient

from utilities.mongo import check_or_create_collection
from utilities.os_util import get_dir
from utilities.time_management import get_today, get_date_string, start, stop
from utilities.constants import *
from utilities.entities.Collection import Collection


ROOT = get_dir(__file__)
JAVASCRIPT_PATH = join(ROOT, JAVASCRIPT_DIR)


TODAY = get_today()
COLLECTION_NAME = RAW_COLLECTION + get_date_string(TODAY)
RESULTS_COLLECTION_NAME = RESULTS_COLLECTION + get_date_string(TODAY)

check_or_create_collection(TWEETS_DB, TEMP_RAW_COLLECTION, Collection.TEMP)
check_or_create_collection(TWEETS_DB, COLLECTION_NAME, Collection.RAW)
check_or_create_collection(TWEETS_DB, TEMP_RESULTS_COLLECTION, Collection.RESULT)

client = MongoClient()
db = client.tweets
coll = db[COLLECTION_NAME]
temp_raw = db[TEMP_RAW_COLLECTION]
temp_results = db[TEMP_RESULTS_COLLECTION]


def execute():
    print 'Started Entity Aggregation... ',

    start()

    map_function = Code(open(join(JAVASCRIPT_PATH, MAP_FUNCTION_FILENAME), 'r').read())
    reduce_function = Code(open(join(JAVASCRIPT_PATH, REDUCE_FUNCTION_FILENAME), 'r').read())
    aggregate_map_function = Code(open(join(JAVASCRIPT_PATH, AGGREGATION_MAP_ADD_FUNCTION_FILENAME), 'r').read())
    aggregate_reduce_function = Code(open(join(JAVASCRIPT_PATH, AGGREGATION_REDUCE_FUNCTION_FILENAME), 'r').read())

    temp_raw.map_reduce(map_function, reduce_function, TEMP_RESULTS_COLLECTION)
    temp_results.map_reduce(aggregate_map_function, aggregate_reduce_function, {'reduce': RESULTS_COLLECTION_NAME})

    # if temp_raw.count() > 0:
    #     coll.insert_many(temp_raw.find())
    temp_results.drop()
    # temp_raw.drop() # TODO
    client.close()
    print 'Finished'
    stop()


if __name__ == '__main__':
    execute()
