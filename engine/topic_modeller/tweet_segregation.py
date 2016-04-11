'''

    Iterate over all tweets in each of the 100 collections.
    Each tweet has to be categorized into a topic.

    As each hashtag normally falls into one category, try to find percentage match to a topic and assign
    all tweets in the collection to the best matched topic.

    For mentions, each tweet is independently categorized into a topic.

    Also while iterating, find the best tweet that matches a topic, for each topic.
    This can be used to summarize the topic in the homepage.

'''
from gensim import models, corpora
from os.path import join
from pymongo import MongoClient, DESCENDING

from utilities.os_util import get_dir
from utilities.constants import *
from utilities.config import NUMBER_OF_TOP_ENTITIES, NUMBER_OF_TOPICS
from utilities.cleaner import clean
from utilities.time_management import start, stop
from utilities.mongo import check_or_create_collection, copy_into_collection
from utilities.entities.Collection import Collection


ROOT = get_dir(__file__)
DICTIONARY_PATH = join(ROOT, DATA_DIR, 'dict2.dict')
CORPUS_PATH = join(ROOT, DATA_DIR, 'corp.mm')

corpus = corpora.MmCorpus(CORPUS_PATH)
dictionary = corpora.Dictionary.load(DICTIONARY_PATH)
lda = models.LdaModel.load('data/lda2_2.lda')

COLLECTION_NAME = RAW_COLLECTION + '11-04-2016'
RESULTS_COLLECTION_NAME = RESULTS_COLLECTION + '11-04-2016'

client = MongoClient()
db = client.tweets
raw_collection = db[COLLECTION_NAME]
results_coll = db[RESULTS_COLLECTION_NAME]

# # dictionary.doc2bow(doc)
# print 'Started '
# lda = models.LdaModel.load('data/lda1.lda')
# doc = 'hello'
# print lda.get_document_topics(dictionary.doc2bow(doc.split(' ')), minimum_probability=0)
# # for id,prob in lda.get_topic_terms(3):
# #     print dictionary[id], prob

top_tweet = [0]*NUMBER_OF_TOPICS
top_prob = [0]*NUMBER_OF_TOPICS
actual_entity = {}
entity_topic = {}
entity_pseudos = {}


def get_topic_for_entity(cleaned_tweets, original_tweets):

    probs = [0]*NUMBER_OF_TOPICS

    for i, tweet in enumerate(cleaned_tweets):
        distribution = lda.get_document_topics(dictionary.doc2bow(tweet), minimum_probability=0)
        for topic_id, prob in distribution:
            probs[topic_id] += prob
            if prob > top_prob[topic_id]:
                top_prob[topic_id] = prob
                top_tweet[topic_id] = original_tweets[i]

    max_prob = 0
    topic = -1
    for topic_id, prob in enumerate(probs):
        if prob > max_prob:
            topic = topic_id
            max_prob = prob

    return topic


def execute():
    print 'Started'
    start()
    results = results_coll.find(limit=NUMBER_OF_TOP_ENTITIES, no_cursor_timeout=True) \
        .sort([(VALUE + '.' + COUNT, DESCENDING)])
    for result in results:

        tweets = []
        text = []
        lower_entity = result[LOWER_ENTITY]
        entities = result[VALUE][PSEUDONYMS]
        entity_pseudos[lower_entity] = entities

        max_tweets = 0
        for entity in entities:
            c = 0
            for tweet in raw_collection.find({ENTITIES: entity}):
                c += 1
                tweets.append(tweet)
                text.append(tweet[TWEET])
            if c > max_tweets:
                actual_entity[lower_entity] = entity
                max_tweets = c

        text = clean(text)
        topic_id = get_topic_for_entity(text, tweets)
        entity_topic[actual_entity[lower_entity]] = topic_id

    print 'Topics are: '
    for i in range(NUMBER_OF_TOPICS):
        print 'Topic', i, lda.print_topic(i, 20)
        print top_tweet[i]

    print
    print 'Entities: Topic'
    for entity in entity_topic.keys():
        print entity, '-', entity_topic[entity]

    for lower_entity in entity_pseudos.keys():
        for entity in entity_pseudos[lower_entity]:
            topic_id = entity_topic[actual_entity[lower_entity]]
            coll_name = 'topic' + str(topic_id)
            check_or_create_collection(TWEETS_DB, coll_name, Collection.TEMP)
            coll = db[coll_name]
            copy_into_collection(raw_collection.find({ENTITIES: entity}), coll)

    stop()

if __name__ == '__main__':
    execute()