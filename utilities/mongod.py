import pymongo
import tweepy
from datetime import datetime
from utilities.time_management import *
from utilities.constants import *
from utilities.config import *
import pytz
#
# client = pymongo.MongoClient()
# db = client.tweets


def fun(coll):
    for i in coll.find(limit=20).sort([('value', -1)]):
        print i

#
# res = db['result_16-11-2015']
# col = db['raw_16-11-2015']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


api = tweepy.API(auth)
new_tweets = api.search(q='@justinbeiber', count=10, since_id=668299868612526080L)
print new_tweets[0].id
print new_tweets[0].text
print new_tweets[0].created_at.replace(tzinfo=pytz.UTC).astimezone(pytz.timezone('Asia/Kolkata'))
print new_tweets[0]

#text, author.(profile_image_url_https, profile_image_url, screen_name, name, id,668316706423590912

#print col.find_one().keys()
