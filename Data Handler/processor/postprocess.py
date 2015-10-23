from pymongo import MongoClient
from bson.code import Code
from utilities.constants import *
from utilities.util import start, stop
client = MongoClient()
db = client.tweets
coll = db.raw

if __name__ == '__main__':

    start()
    map = Code(open(MAP_FUNCTION,'r').read())
    reduce = Code(open(REDUCE_FUNCTION,'r').read())
    coll.map_reduce(map,reduce,RESULTS_COLLECTION)

    stop()

    print db.collection_names()
