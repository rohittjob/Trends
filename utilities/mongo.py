from pymongo import MongoClient, ASCENDING, DESCENDING
from .constants import *

client = MongoClient()


def init():
    print "Checking if database exists... ",
    if TWEETS_DB in client.database_names():
        print 'YES'
        db = client.tweets
        print "Checking if collection '"+ RAW_COLLECTION +"' exists... ",
        if RAW_COLLECTION in db.collection_names():
            print 'YES'
        else:
            print 'NO'
            print "Creating collection '"+ RAW_COLLECTION +"'... ",
            collection = db[RAW_COLLECTION]
            collection.create_index([(ENTITIES, ASCENDING), (TIMESTAMP, ASCENDING)])
            print 'Created'

        print "Checking if collection '"+ RESULTS_COLLECTION +"' exists... ",
        if RESULTS_COLLECTION in db.collection_names():
            print 'YES'
        else:
            print 'NO'
            print "Creating collection '"+ RESULTS_COLLECTION +"'... ",
            collection = db[RESULTS_COLLECTION]
            collection.create_index([(VALUE, DESCENDING)])
            print 'Created'

    else:
        print 'NO'
        print 'Creating database "tweets"... Created'
        db = client.tweets
        print "Creating collection '"+ RAW_COLLECTION +"'... ",
        collection = db.raw
        collection.create_index([(ENTITIES, ASCENDING), (TIMESTAMP, ASCENDING)])
        print 'Created'
        print "Creating collection '"+ RESULTS_COLLECTION +"'... ",
        collection = db[RESULTS_COLLECTION]
        collection.create_index([(VALUE, DESCENDING)])
        print 'Created'








