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
RAW_COLLECTION = 'raw_'
RESULTS_COLLECTION = 'result_'
WEEKLY_RESULTS_COLLECTION = 'weekly_result_'
VALUE = 'value.count'


# FileNames
MAP_FUNCTION = 'mapFunction.js'
REDUCE_FUNCTION = 'reduceFunction.js'
AGGREGATION_MAP_ADD_FUNCTION = 'aggregationAddMapFunction.js'
AGGREGATION_MAP_SUBTRACT_FUNCTION = 'aggregationSubtractMapFunction.js'
AGGREGATION_REDUCE_FUNCTION = 'aggregationReduceFunction.js'

PREPROCESSOR = 'preprocess.py'
POSTPROCESSOR = 'postprocess.py'
DAILY_AGGREGATOR = 'daily_aggregation.py'
WEEKLY_AGGREGATOR = 'weekly_aggregation.py'
EXTRACTOR = 'tweet_extractor.py'

DATA_FILE_PREFIX = 'data'

# Directories

EXTRACTOR_DIR = 'extractor'
PROCESSOR_DIR = 'processor'
DATA_HANDLER_DIR = 'Data Handler'
EXTRACTOR_DATA_DIR = 'data'
PREPROCESSOR_TEMP_DIR = 'temp'


JSON = '.json'
