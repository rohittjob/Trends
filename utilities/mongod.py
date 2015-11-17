import pymongo
from datetime import datetime
from utilities.time_management import *
from utilities.constants import *
from utilities.config import *
import pytz

client = pymongo.MongoClient()
db = client.tweets


def fun(coll):
    for i in coll.find(limit=20).sort([('value', -1)]):
        print i


res = db['result_16-11-2015']
col = db['raw_16-11-2015']
fun(res)
print db.collection_names()
