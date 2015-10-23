DATETIME_FORMAT = '%a %b %d %H:%M:%S +0000 %Y'

# keys in twitter JSON

CREATED_AT = 'created_at'
ENTITIES = 'entities'
TEXT = 'text'
RETWEET_COUNT = 'retweet_count'
ID = 'id'
USER = 'user'
SCREEN_NAME = 'screen_name'
PLACE = 'place'
COORDINATES = 'coordinates'
HASHTAGS = 'hashtags'
MENTIONS = 'user_mentions'
URLS = 'urls'
URL = 'url'


TIMESTAMP = 'Timestamp'
TWEET = 'Tweet'
RETWEETS = 'Retweets'
USERNAME = 'Username'

# Mongo database literals

TWEETS_DB = 'tweets'
RAW_COLLECTION = 'raw'
RESULTS_COLLECTION = 'map_reduce_results'
VALUE = 'value.count'

# time constants

SECONDS = 1
MINUTES = 60 * SECONDS
HOURS = 60*MINUTES

PREPROCESS_SLEEP_TIME = 10*MINUTES

# FileNames
MAP_FUNCTION = 'mapFunction.js'
REDUCE_FUNCTION = 'reduceFunction.js'

JSON = '.json'
