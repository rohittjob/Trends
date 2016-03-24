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
TEMP_RAW_COLLECTION = 'raw_temp'
TEMP_RESULTS_COLLECTION = 'result_temp'
VALUE = 'value'
TAG = '_id'


# FileNames
MAP_FUNCTION = 'mapFunction.js'
REDUCE_FUNCTION = 'reduceFunction.js'
AGGREGATION_MAP_ADD_FUNCTION = 'aggregationAddMapFunction.js'
AGGREGATION_MAP_SUBTRACT_FUNCTION = 'aggregationSubtractMapFunction.js'
AGGREGATION_REDUCE_FUNCTION = 'aggregationReduceFunction.js'

MONGO_INIT_FILE = 'start_mongo.bat'
ENGINE_MANAGER = 'manager.py'
PREPROCESSOR = 'preprocess.py'
DAILY_AGGREGATOR = 'daily_aggregation.py'
WEEKLY_AGGREGATOR = 'weekly_aggregation.py'
EXTRACTOR = 'tweet_extractor.py'
PROCESSOR = 'process.py'
TRENDS_EXTRACTOR = 'trends_extractor.py'
GRAPH_APPROXIMATOR = 'graph_approximation.py'
WEEKLY_PROCESSOR = 'weekly_process.py'

DJANGO_MANAGER = 'manage.py'
RUNSERVER_COMMAND = 'runserver'

DATA_FILE_PREFIX = 'data'

REQUIREMENTS = 'requirements.txt'
PIP_INSTALL_FILE = 'get-pip.py'
PYTHON_INSTALL_FILE = 'python_install.lnk'
MONGO_INSTALL_FILE = 'mongo_install.lnk'

# Directories

JAVASCRIPT_DIR = 'javascript'
EXTRACTOR_DIR = 'extractor'
PROCESSOR_DIR = 'processor'
DATA_HANDLER_DIR = 'Data Handler'
EXTRACTOR_DATA_DIR = 'data'
PREPROCESSOR_TEMP_DIR = 'temp'
ENGINE_DIR = 'engine'
MISCELLANEOUS_DIR = 'miscellaneous'
DEPENDENCIES_DIR = 'dependencies'
BATCH_DIR = 'batch'
MONGO_DIR = 'MongoDB'

WEBSITE_DIR = 'website'
STATIC_DIR = 'static'
TSV_DIR = 'tsv'

WHEELHOUSE = 'wheelhouse'

# Processes

MANAGER = 'Manager'
PROCESSOR_PROCESS = 'Processor'

# MongoDB operators

LESS_THAN = '$lt'
GREATER_THAN_OR_EQUAL = '$gte'

JSON = '.json'
TSV = '.tsv'
