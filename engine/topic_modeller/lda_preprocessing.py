from gensim import corpora
from pymongo import MongoClient, DESCENDING
from os.path import join

from utilities.os_util import get_dir
from utilities.time_management import get_today, get_date_string, start, stop
from utilities.constants import *
from utilities.config import NUMBER_OF_TOP_ENTITIES, TWEET_POOLING_SIZE
from utilities.cleaner import clean


ROOT = get_dir(__file__)
DICTIONARY_PATH = join(ROOT, DATA_DIR, 'dict2.dict')
CORPUS_PATH = join(ROOT, DATA_DIR, 'corp.mm')

TODAY = get_today()
COLLECTION_NAME = RAW_COLLECTION + '11-04-2016'
RESULTS_COLLECTION_NAME = RESULTS_COLLECTION + '11-04-2016'

client = MongoClient()
db = client.tweets
raw_collection = db[COLLECTION_NAME]
results_coll = db[RESULTS_COLLECTION_NAME]


def get_documents():
    documents = []
    results = results_coll.find(limit=NUMBER_OF_TOP_ENTITIES, no_cursor_timeout=True)\
                          .sort([(VALUE + '.' + COUNT, DESCENDING)])
    for result in results:
        entities = result[VALUE][PSEUDONYMS]
        for entity in entities:
            cnt = 0
            document = ''
            for tweet in raw_collection.find({ENTITIES: entity}):
                cnt += 1
                document += tweet[TWEET] + ' '
                if cnt == TWEET_POOLING_SIZE:
                    documents.append(document)
                    document = ''
                    cnt = 0
            if document != '':
                documents.append(document)

    results.close()

    return documents


def execute():
    start()
    print 'Starting PreProcessing'

    documents = get_documents()
    tokenized_documents = clean(documents)

    print tokenized_documents

    dictionary = corpora.Dictionary([doc for doc in tokenized_documents])
    dictionary.compactify()
    dictionary.save(DICTIONARY_PATH)

    corpus = [dictionary.doc2bow(doc) for doc in tokenized_documents]
    corpora.MmCorpus.serialize(CORPUS_PATH, corpus)

    stop()

    client.close()


if __name__ == '__main__':
    execute()
