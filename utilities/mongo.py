from pymongo import MongoClient, ASCENDING, DESCENDING

from utilities.constants import VALUE, ENTITIES, TIMESTAMP, TAG, RAW_COLLECTION
from utilities.time_management import *
from utilities.config import WEEK_RANGE

client = MongoClient()


def check_collection(db, coll):
    if db in client.database_names():
        db = client[db]
        if coll in db.collection_names():
            print 'Collection ' + coll + ' exists!!!'
            return True
    return False


def create_result(db, coll):
    if not check_collection(db, coll):
        print 'Creating collection ' + coll + '!!!'
        db = client[db]
        coll = db[coll]
        coll.create_index([(VALUE, DESCENDING)])


def create_raw(db, coll):
    if not check_collection(db, coll):
        print 'Creating collection ' + coll + '!!!'
        db = client[db]
        coll = db[coll]
        coll.create_index([(ENTITIES, ASCENDING), (TIMESTAMP, ASCENDING)])


HASHTAG = 1
MENTION = 2


def extract_top_entities(coll):
    results = []
    for top_result in coll.find(limit=100).sort([('value', -1)]):
        results.append(top_result[TAG])
    return results


def get_type(entity):
    if entity[0] == '#':
        return HASHTAG
    else:
        return MENTION


def get_week_raw_collections(week_start):
    week_coll = []
    day = week_start
    for i in range(WEEK_RANGE):
        coll_name = RAW_COLLECTION + get_date_string(day)
        day = get_next_day(day)
        week_coll.append(coll_name)

    return week_coll

