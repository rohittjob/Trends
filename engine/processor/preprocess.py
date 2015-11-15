from engine.utilities.os_util import *
from engine.utilities.miscellaneous import check_percent
from engine.utilities.time_management import *
from engine.utilities.mongo import *
from engine.utilities.constants import *

from pymongo import MongoClient
from os import remove
import pytz
import json


ROOT = dirname(get_dir(__file__))
TEMP_PATH = join(ROOT, EXTRACTOR_DIR, PREPROCESSOR_TEMP_DIR)
TODAY = get_today() 

create_raw(TWEETS_DB, TEMP_RAW_COLLECTION)

client = MongoClient()
db = client.tweets
collection = db[TEMP_RAW_COLLECTION]


def extract_data(file_path):  # load json file into a list of dictionaries
    tweets_data = []
    tweets_file = open(file_path, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue
    tweets_file.close()
    return tweets_data


def extract_time(date):
    date = datetime.strptime(date, DATETIME_FORMAT)
    date.replace(tzinfo=pytz.UTC)
    return date


def get_hash_and_mentions(entities):
    new_entities = []
    hashtags = entities[HASHTAGS]
    mentions = entities[MENTIONS]

    for hashtag in hashtags:
        new_entities.append('#'+hashtag[TEXT])
    for mention in mentions:
        new_entities.append('@'+mention[SCREEN_NAME])

    return new_entities


def get_urls(entities):
    urls = []
    for url in entities[URLS]:
        urls.append(url[URL])
    return urls


def process(tweets_data):  # extract relevant information from tweets
    new_data = []
    for tweet in tweets_data:
        try:
            new_tweet = {ENTITIES: get_hash_and_mentions(tweet[ENTITIES])}
            if len(new_tweet[ENTITIES]) == 0:  # checking if tweet has hashtags or user mentions
                continue

            new_tweet[TIMESTAMP] = extract_time(tweet[CREATED_AT])
            new_tweet[USERNAME] = tweet[USER][SCREEN_NAME]
            new_tweet[TWEET] = tweet[TEXT]
            new_tweet[RETWEETS] = tweet[RETWEET_COUNT]

            new_tweet[URLS] = get_urls(tweet[ENTITIES])

            new_tweet[COORDINATES] = tweet[COORDINATES]
            new_tweet[PLACE] = tweet[PLACE]
            new_tweet[ID] = tweet[ID]
            new_data.append(new_tweet)
        except:
            'Tweet Error'
            print tweet
    return new_data


if __name__ == '__main__':

    print "Started Preprocessing... ",
    data_files = get_files_in_dir(TEMP_PATH, JSON)
    l = len(data_files)
    cnt = 0
    completed_percentage = check_percent(cnt, l, 5, 0)
    start()
    for data_file in data_files:
        file_path = join(TEMP_PATH, data_file)
        cnt += 1
        tweets_data = extract_data(file_path)
        new_data = process(tweets_data)
        collection.insert_many(new_data)
        remove(file_path)
        completed_percentage = check_percent(cnt, l, 5, completed_percentage)

    print
    print 'Finished'
    stop()
