from utilities.time_management import *
from utilities.config import DAY_START, APPROXIMATION_RANGE, WEEK_RANGE
from utilities.constants import *
from utilities.mongo import *
from utilities.os_util import *
import os
import django
import pymongo

os.environ["DJANGO_SETTINGS_MODULE"] = "portal.settings"
django.setup()
from home.models import *

ROOT = dirname(dirname(get_dir(__file__)))
TSV_DIR_PATH = join(ROOT, WEBSITE_DIR, STATIC_DIR, TSV_DIR)


TODAY = get_safe_today()
TODAY = localize_datetime(TODAY)
WEEK_START = get_week_start(TODAY)

WEEK_COLLECTIONS = get_week_raw_collections(WEEK_START)

client = pymongo.MongoClient()
db = client.tweets

entities = []


def remove_previous_data():
    tsv_files = get_files_in_dir(TSV_DIR_PATH, TSV)
    for tsv_file in tsv_files:
        os.remove(join(TSV_DIR_PATH, tsv_file))


def init_collections():
    for coll in WEEK_COLLECTIONS:
        create_raw(TWEETS_DB, coll)


def get_entities():
    global entities
    for item in TopHashTags.objects.all():
        entities.append(item.hashtag)
    for item in TopUserMentions.objects.all():
        entities.append(item.mentioned_user)


def init_writer(entity):
    entity = entity.lower()
    if get_type(entity) == HASHTAG:
        prefix = 'H_'
    else:
        prefix = 'M_'
    file_path = join(TSV_DIR_PATH, prefix + entity[1:] + TSV)
    x = open(file_path, "w")
    x.write('datetime\tcount\n')
    return x


def close_writer(writer):
    writer.close()


def make_entry(writer, obj, count):
    writer.write(get_date_time_string(obj) + '\t' + str(count) + '\n')


def generate_graph_data_for_day(entity, coll_name, day, next_day_start, writer):
    coll = db[coll_name]
    lower = get_datetime_from_string(day, DAY_START)
    upper = lower + APPROXIMATION_RANGE
    while upper <= next_day_start:
        tweet_count = coll.find({ENTITIES: entity, TIMESTAMP: {GREATER_THAN_OR_EQUAL: lower, LESS_THAN: upper}}).count()
        make_entry(writer, lower, tweet_count*100)
        lower += APPROXIMATION_RANGE
        upper += APPROXIMATION_RANGE


def generate_graph_data(entity):
    writer = init_writer(entity)
    day = WEEK_START
    for i in range(WEEK_RANGE):
        coll_name = RAW_COLLECTION + get_date_string(day)
        next_day = get_next_day(day)
        next_day_start = get_datetime_from_string(next_day, DAY_START)
        generate_graph_data_for_day(entity, coll_name, day, next_day_start, writer)
        day = next_day

    close_writer(writer)


if __name__ == '__main__':
    init_collections()
    remove_previous_data()
    print "Extracting entities... ",
    get_entities()
    print 'Done'
    for entity in entities:
        print 'Generating data points for ' + entity + '... ',
        generate_graph_data(entity)
        print 'Done'
    client.close()






