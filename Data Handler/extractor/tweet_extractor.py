# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from os import rename
from utilities.os_util import *
from utilities.config import *
from utilities.constants import *

# Variables that contains the user credentials to access Twitter API
access_token = "2583390259-eRijiycaorQHFeVGTI2YNfT6kc9JWtNSOdwlfnR"
access_token_secret = "IWhMPVdw9sdSJ4ex20ObFgS2BbGLxo3nWHyqp4sy4Bga2"
consumer_key = "SVI97pI1bbxjHOevoGoyCUH5X"
consumer_secret = "anAQ83bkPT7JmIEvPssQ8CbP2tUmADq9Jn68VdHg1HiROcoJr2"


FILESIZE_LIMIT = MAX_TWEETS_IN_FILE
DISPLAY_INTERVAL = DISPLAY_COMPLETED_TWEETS_INTERVAL
FILE_NUMBER_LIMIT = FILE_NUMBER_RESET_VALUE
FILE_NAME_FORMATTER = '%0' + str(FILE_NAME_SUFFIX_DIGITS) + 'd'

display_number = DISPLAY_INTERVAL

file_number = 1
cnt = 0

ROOT = get_dir(__file__)

FILE_PATH = join(ROOT, EXTRACTOR_DATA_DIR)
TEMP_PATH = join(ROOT, PREPROCESSOR_TEMP_DIR)


def get_filename(directory, number):
    return join(directory, DATA_FILE_PREFIX + FILE_NAME_FORMATTER % number + JSON)


file_name = get_filename(FILE_PATH, file_number)
tweets_file = open(file_name, "w")


def change_file():
    global tweets_file, file_name, file_number, display_number

    tweets_file.close()
    display_number = DISPLAY_INTERVAL
    rename(file_name, get_filename(TEMP_PATH, file_number))  # moving file to temp folder

    file_number += 1
    if file_number == FILE_NUMBER_LIMIT:
        file_number = 1

    file_name = get_filename(FILE_PATH, file_number)
    tweets_file = open(file_name, "w")


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        if not (data[2] == 'c' and data[3] == 'r'):  # checking if invalid tweet
            return True

        global cnt, file_number, tweets_file, file_name, display_number
        cnt += 1
        tweets_file.write(data)

        if cnt == display_number:
            print str(display_number) + ' Tweets Downloaded'
            display_number += DISPLAY_INTERVAL

        if cnt == FILESIZE_LIMIT:
            cnt = 0
            change_file()

        return True

    def on_error(self, status):
        print 'error: ' + status


if __name__ == '__main__':

    while True:  # ensures continuous stream extraction
        try:
            # This handles Twitter authentication and the connection to Twitter Streaming API

            l = StdOutListener()
            auth = OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            stream = Stream(auth, l)

            # This line filter Twitter Streams to capture data by the top 20 most used keywords from the following URL:
            # http://techland.time.com/2009/06/08/the-500-most-frequently-used-words-on-twitter/

            stream.filter(languages=["en"], track=["a", "the", "i", "you", "to", "and", "is", "in", "u", "of", "it"])
        except:
            continue
