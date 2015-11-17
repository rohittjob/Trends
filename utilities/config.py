from datetime import timedelta

# General

PYTHON_VERSION = '2.7.10'
TIMEZONE = 'Asia/Kolkata'

# time constants

SECONDS = 1
MINUTES = 60 * SECONDS
HOURS = 60*MINUTES

# Preprocessor
PROCESSOR_SLEEP_TIME = 10*MINUTES

# Extractor
MAX_TWEETS_IN_FILE = 10000
DISPLAY_COMPLETED_TWEETS_INTERVAL = 1000

FILE_NUMBER_RESET_VALUE = 100
FILE_NAME_SUFFIX_DIGITS = 2

# Manager Process
DEBUG = True
STOP_DATA_EXTRACTION_TIME = '23:55'
RESTART_DATA_EXTRACTION_TIME = '00:05'
WEEK_RANGE = 7  # Represents number of days in a week

CHECK_SAFE_DATE_TIME = '01:00'  # This is to check if TODAY is actually the day in consideration


# Graph Approximation

DAY_START = '00:00'
APPROXIMATION_RANGE = timedelta(hours=1)

