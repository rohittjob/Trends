from time import sleep
from pymongo import MongoClient
from datetime import datetime
from utilities.constants import *
from utilities.os_util import *
from utilities.util import start, stop, check_percent
import pytz, json


ROOT = dirname(get_dir(__file__))
TEMP_PATH = join(ROOT,'extractor','temp')


client = MongoClient()
db = client.tweets
collection = db.raw1


def extract_data(file_path): # load json file into a list of dictionaries
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
    date = datetime.strptime(date,DATETIME_FORMAT)
    date.replace(tzinfo= pytz.UTC)
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


def getURLs(entities):
    urls = []
    for url in entities[URLS]:
        urls.append(url[URL])
    return urls


def process(tweets_data): # extract relevant information from tweets
    new_data = []
    for tweet in tweets_data:
        new_tweet = {}
        new_tweet[ENTITIES] = get_hash_and_mentions(tweet[ENTITIES])

        if len(new_tweet[ENTITIES]) == 0:  # checking if tweet has hashtags or user mentions
            continue

        new_tweet[TIMESTAMP] = extract_time(tweet[CREATED_AT])
        new_tweet[USERNAME] = tweet[USER][SCREEN_NAME]
        new_tweet[TWEET] = tweet[TEXT]
        new_tweet[RETWEETS] = tweet[RETWEET_COUNT]

        new_tweet[URLS] = getURLs(tweet[ENTITIES])

        new_tweet[COORDINATES] = tweet[COORDINATES]
        new_tweet[PLACE] = tweet[PLACE]
        new_tweet[ID] = tweet[ID]
        new_data.append(new_tweet)
    return new_data


if __name__ == '__main__':

    print "Started Preprocessing"
    files = get_files_in_dir(TEMP_PATH,JSON)
    l = len(files)
    cnt = 0
    completed_percentage = check_percent(cnt, l, 5, 0)
    start()
    for file in files:
        cnt += 1
        tweets_data = extract_data(join(TEMP_PATH,file))
        new_data = process(tweets_data)
        collection.insert_many(new_data)
        completed_percentage = check_percent(cnt, l, 5, completed_percentage)
    print
    stop()





