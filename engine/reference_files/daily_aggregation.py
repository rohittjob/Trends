from os.path import join

from bson.code import Code
from utilities.mongo import *
from utilities.os_util import *
from utilities.time_management import *
from utilities.constants import *
from pymongo import MongoClient


ROOT = get_dir(__file__)
JAVASCRIPT = join(ROOT, JAVASCRIPT_DIR)


TODAY = get_today()
COLLECTION_NAME = RAW_COLLECTION + get_date_string(TODAY)
RESULTS_COLLECTION_NAME = RESULTS_COLLECTION + get_date_string(TODAY)

create_raw(TWEETS_DB, TEMP_RAW_COLLECTION)
create_raw(TWEETS_DB, COLLECTION_NAME)
create_result(TWEETS_DB, TEMP_RESULTS_COLLECTION)

client = MongoClient()
db = client.tweets
coll = db[COLLECTION_NAME]
temp_raw = db[TEMP_RAW_COLLECTION]
temp_results = db[TEMP_RESULTS_COLLECTION]

if __name__ == '__main__':

    print 'Started Daily Aggregation... ',

    start()

    map_function = Code(open(join(JAVASCRIPT, MAP_FUNCTION), 'r').read())
    reduce_function = Code(open(join(JAVASCRIPT, REDUCE_FUNCTION), 'r').read())
    aggregate_map_function = Code(open(join(JAVASCRIPT, AGGREGATION_MAP_ADD_FUNCTION), 'r').read())
    aggregate_reduce_function = Code(open(join(JAVASCRIPT, AGGREGATION_REDUCE_FUNCTION), 'r').read())

    temp_raw.map_reduce(map_function, reduce_function, TEMP_RESULTS_COLLECTION)
    temp_results.map_reduce(aggregate_map_function, aggregate_reduce_function, {'reduce': RESULTS_COLLECTION_NAME})

    if temp_raw.count() > 0:
        coll.insert_many(temp_raw.find())
    temp_results.drop()
    temp_raw.drop()
    client.close()
    print 'Finished'
    stop()
