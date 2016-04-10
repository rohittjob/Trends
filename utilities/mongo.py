from pymongo import MongoClient, ASCENDING, DESCENDING

from utilities.constants import VALUE, ENTITIES, TIMESTAMP, TAG, RAW_COLLECTION, ID
from utilities.time_management import *
from utilities.entities.Collection import Collection
from utilities.config import WEEK_RANGE

client = MongoClient()


def check_collection(db, coll):
    if db in client.database_names():
        db = client[db]
        if coll in db.collection_names():
            print 'Collection ' + coll + ' exists!!!'
            return True
    return False


def create_index(coll, coll_type=None):
    if coll_type == Collection.RAW:
        coll.create_index([(ENTITIES, ASCENDING), (TIMESTAMP, ASCENDING)])
    elif coll_type == Collection.RESULT:
        coll.create_index([(VALUE, DESCENDING)])
    elif coll_type == Collection.TEMP:
        coll.create_index([(ID, ASCENDING)], unique=True)


def check_or_create_collection(db, coll_name, coll_type=None):
    if not check_collection(db, coll_name):
        print 'Creating collection ' + coll_name + '!!!'
        db = client[db]
        coll = db[coll_name]
        create_index(coll, coll_type)


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


def copy_collection(col1, col2):

    c = 0
    tw = []
    cur = col1.find(no_cursor_timeout=True)
    for t in cur:
        c += 1
        tw.append(t)
        if c == 10000:
            c = 0
            tw = []
            col2.insert_many(tw)

    col2.insert_many(tw)    # transfer remaining
    cur.close()

