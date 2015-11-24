# Import the necessary methods from tweepy library
from os import rename

from utilities.config import *
from utilities.miscellaneous import is_json
from utilities.os_util import *
from utilities.constants import *
from utilities.time_management import get_time
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener



FILESIZE_LIMIT = MAX_TWEETS_IN_FILE
DISPLAY_INTERVAL = DISPLAY_COMPLETED_TWEETS_INTERVAL
FILE_NUMBER_LIMIT = FILE_NUMBER_RESET_VALUE
FILE_NAME_FORMATTER = '%0' + str(FILE_NAME_SUFFIX_DIGITS) + 'd'

display_number = DISPLAY_INTERVAL

file_number = 1
file_cnt = 0
total_cnt = 0

ROOT = get_dir(__file__)

FILE_PATH = join(ROOT, EXTRACTOR_DATA_DIR)
TEMP_PATH = join(ROOT, PREPROCESSOR_TEMP_DIR)


def get_filename(directory, number):
    return join(directory, DATA_FILE_PREFIX + FILE_NAME_FORMATTER % number + JSON)


file_name = get_filename(FILE_PATH, file_number)
tweets_file = open(file_name, "w")


def change_file():
    global tweets_file, file_name, file_number

    tweets_file.close()
    rename(file_name, get_filename(TEMP_PATH, file_number))  # moving file to temp folder

    file_number += 1
    if file_number == FILE_NUMBER_LIMIT:
        file_number = 1

    file_name = get_filename(FILE_PATH, file_number)
    tweets_file = open(file_name, "w")


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):

        if not is_json(data):  # checking if invalid tweet
            return True
        global file_cnt, file_number, tweets_file, file_name, display_number, total_cnt
        file_cnt += 1
        total_cnt += 1
        tweets_file.write(data)

        if total_cnt == display_number:
            print '\r',
            print str(display_number) + ' Tweets Downloaded',
            display_number += DISPLAY_INTERVAL

        if file_cnt == FILESIZE_LIMIT:
            file_cnt = 0
            change_file()

        return True

    def on_error(self, status):
        print 'error: ' + status


if __name__ == '__main__':

    print "Started extracting tweets at " + get_time() + "... "

    while True:  # ensures continuous stream extraction
        try:
            # This handles Twitter authentication and the connection to Twitter Streaming API

            l = StdOutListener()
            auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
            stream = Stream(auth, l)

            # This line filter Twitter Streams to capture data by the top 20 most used keywords from the following URL:
            # http://techland.time.com/2009/06/08/the-500-most-frequently-used-words-on-twitter/

            stream.filter(languages=["en"], track=["a", "the", "i", "you", "to", "and", "is", "in", "u", "of", "it"])
        except:
            continue
