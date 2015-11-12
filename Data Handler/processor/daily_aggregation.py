from pymongo import MongoClient
from bson.code import Code
from utilities.constants import *
from utilities.time_management import *
from utilities.os_util import *
from os.path import join

ROOT = get_dir(__file__)

TODAY = get_today()
COLLECTION_NAME = RAW_COLLECTION + get_date_string(TODAY)
RESULTS_COLLECTION_NAME = RESULTS_COLLECTION + get_date_string(TODAY)

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
