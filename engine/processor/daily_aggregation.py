from pymongo import MongoClient
from bson.code import Code
from engine.utilities.constants import *
from engine.utilities.time_management import *
from engine.utilities.os_util import *
from engine.utilities.mongo import *
from os.path import join

ROOT = get_dir(__file__)


def check(collection):
    if not check_collection(TWEETS_DB, collection):
        create_raw(TWEETS_DB, collection)

TODAY = get_today()
COLLECTION_NAME = RAW_COLLECTION + get_date_string(TODAY)
RESULTS_COLLECTION_NAME = RESULTS_COLLECTION + get_date_string(TODAY)

check(COLLECTION_NAME)

client = MongoClient()
db = client.tweets
coll = db[COLLECTION_NAME]

if __name__ == '__main__':

    print 'Started Daily Aggregation... ',

    start()

    map_function = Code(open(join(ROOT, MAP_FUNCTION), 'r').read())
    reduce_function = Code(open(join(ROOT, REDUCE_FUNCTION), 'r').read())
    coll.map_reduce(map_function, reduce_function, RESULTS_COLLECTION_NAME)

    print 'Finished'
    stop()
