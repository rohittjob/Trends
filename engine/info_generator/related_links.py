'''

    Find the most frequently shared URLs for each topic.
    Use MapReduce if needed, simple count can also be used depending on the average number
    of URLs per topic.
    Try to add more intelligence to neglect unrelated URLs etc. Might be tough, some research may
    shed simple methods.

'''
from os.path import join
from bson.code import Code
from pymongo import MongoClient, DESCENDING

from utilities.mongo import check_or_create_collection
from utilities.os_util import get_dir
from utilities.time_management import start, stop
from utilities.constants import *
from utilities.entities.Collection import Collection
from utilities.config import NUMBER_OF_TOPICS


ROOT = get_dir(__file__)
JAVASCRIPT_PATH = join(ROOT, JAVASCRIPT_DIR)
TSV_DIR_PATH = join(ROOT, TSV_DIR)

client = MongoClient()
db = client.tweets

MAP_FUNCTION = Code(open(join(JAVASCRIPT_PATH, MAP_FUNCTION_FILENAME), 'r').read())
REDUCE_FUNCTION = Code(open(join(JAVASCRIPT_PATH, REDUCE_FUNCTION_FILENAME), 'r').read())


def write_urls(topic_id, urls):
    file_path = join(TSV_DIR_PATH, 'topic' + str(topic_id) + TSV)
    x = open(file_path, 'w')
    for url in urls:
        x.write(url + '\n')

    x.close()


def aggregate_urls():
    for topic_id in range(NUMBER_OF_TOPICS):
        coll_name = 'topic' + str(topic_id)
        results_coll_name = TOPIC_URL_AGGR_COLLECTION(topic_id)

        check_or_create_collection(RAW_TWEETS_DB, coll_name, Collection.TEMP)
        check_or_create_collection(RAW_TWEETS_DB, results_coll_name, Collection.RESULT)

        coll = db[coll_name]
        coll.map_reduce(MAP_FUNCTION, REDUCE_FUNCTION, results_coll_name)


def execute():
    print 'Started Entity Aggregation... ',

    aggregate_urls()

    start()
    for topic_id in range(NUMBER_OF_TOPICS):
        results_coll_name = TOPIC_URL_AGGR_COLLECTION(topic_id)
        results_coll = db[results_coll_name]

        top_urls = []
        results = results_coll.find(limit=15).sort([(VALUE, DESCENDING)])
        for result in results:
            top_urls.append(result[GENERAL_ID_TAG])

        write_urls(topic_id, top_urls)

    client.close()
    print 'Finished'
    stop()


if __name__ == '__main__':
    execute()

