
from pymongo import MongoClient, DESCENDING
from datetime import datetime
from utilities.constants import *
client = MongoClient()
print client.tweets[RESULTS_COLLECTION].find_one()
#
# print client.tweets[RESULTS_COLLECTION].find_one()
# for i in client.tweets[RESULTS_COLLECTION].find(limit=5).sort([('value.count',-1)]):
#     print i


