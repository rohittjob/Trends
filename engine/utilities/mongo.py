from pymongo import MongoClient, ASCENDING, DESCENDING
from engine.utilities.constants import VALUE, ENTITIES, TIMESTAMP

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
