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
EXPANDED_URL = 'expanded_url'
RETWEETED_STATUS = 'retweeted_status'
LOWER_ENTITY = '_id'


TIMESTAMP = 'Timestamp'
TWEET = 'Tweet'
RETWEETS = 'Retweets'
USERNAME = 'Username'

# Mongo database literals

TWEETS_DB = 'tweets'
RAW_COLLECTION = 'raw_'
RESULTS_COLLECTION = 'entity_result_'
TEMP_RAW_COLLECTION = 'raw_temp'
TEMP_RESULTS_COLLECTION = 'result_temp'
URL_RESULTS_COLLECTION = 'url_result_'


def TOPIC_URL_AGGR_COLLECTION(topic_id):
    return URL_RESULTS_COLLECTION + str(topic_id)

VALUE = 'value'
COUNT = 'count'
PSEUDONYMS = 'pseudos'
TAG = '_id'


# FileNames
MAP_FUNCTION_FILENAME = 'mapFunction.js'
REDUCE_FUNCTION_FILENAME = 'reduceFunction.js'
AGGREGATION_MAP_ADD_FUNCTION_FILENAME = 'aggregationAddMapFunction.js'
AGGREGATION_MAP_SUBTRACT_FUNCTION_FILENAME = 'aggregationSubtractMapFunction.js'
AGGREGATION_REDUCE_FUNCTION_FILENAME = 'aggregationReduceFunction.js'

MONGO_INIT_FILE = 'start_mongo.bat'
ENGINE_MANAGER = 'manager.py'
PREPROCESSOR = 'preprocess.py'
ENTITY_AGGREGATOR = 'entity_aggregation.py'
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

# LDA Files

DICTIONARY = 'dictionary.dict'
CORPUS = 'corpus.mm'


# Directories

JAVASCRIPT_DIR = 'javascript'
EXTRACTOR_DIR = 'extractor'
PROCESSOR_DIR = 'processor'
DATA_HANDLER_DIR = 'Data Handler'
DATA_DIR = 'data'
TEMP_DIR = 'temp'
TEMP = 'temp2'
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



