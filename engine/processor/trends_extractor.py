import pymongo
from utilities.time_management import *
from utilities.constants import *
from utilities.mongo import *
import os
import django
os.environ["DJANGO_SETTINGS_MODULE"] = "portal.settings"
django.setup()

from home.models import *

client = pymongo.MongoClient()
db = client.tweets

results = []
hash_count = 0
mention_count = 0


TODAY = get_safe_today()
WEEK_START = get_week_start(TODAY)


RESULTS_COLLECTION_NAME = WEEKLY_RESULTS_COLLECTION + get_date_string(WEEK_START)
result_db = db[RESULTS_COLLECTION_NAME]


if __name__ == '__main__':

    TopHashTags.objects.all().delete()
    TopUserMentions.objects.all().delete()

    print 'Extracting Top Entities... ',
    results = extract_top_entities(result_db)
    print 'Extracted'
    print 'Finding Top 5 Hashtags and User Mentions... ',
    for result in results:
        if get_type(result) == HASHTAG:
            if hash_count < 5:
                hash_count += 1
                TopHashTags(hashtag=result, rank=hash_count).save()
            elif mention_count == 5:
                break

        else:
            if mention_count < 5:
                mention_count += 1
                TopUserMentions(mentioned_user=result, rank=mention_count).save()
            elif hash_count == 5:
                break
    client.close()

    print 'Done'
