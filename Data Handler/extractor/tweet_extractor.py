#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from os.path import join
from os import rename
from utilities.os_util import *

#Variables that contains the user credentials to access Twitter API 
access_token = "2583390259-eRijiycaorQHFeVGTI2YNfT6kc9JWtNSOdwlfnR"
access_token_secret = "IWhMPVdw9sdSJ4ex20ObFgS2BbGLxo3nWHyqp4sy4Bga2"
consumer_key = "SVI97pI1bbxjHOevoGoyCUH5X"
consumer_secret = "anAQ83bkPT7JmIEvPssQ8CbP2tUmADq9Jn68VdHg1HiROcoJr2"


FILESIZE_LIMIT = 1000
DISPLAY_LIMIT = 100

display_number = DISPLAY_LIMIT

file_number = 1
cnt = 0

ROOT = get_dir(__file__)

FILE_PATH = join(ROOT,'data')
TEMP_PATH = join(ROOT,'temp')

file_name = join(FILE_PATH,'data'+str(file_number)+'.json')
tweets_file = open(file_name, "w")

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        if not (data[2]=='c' and data[3]=='r'): # checking if valid tweet
            return True
        global cnt, file_number, tweets_file, file_name, display_number
        cnt+=1
        tweets_file.write(data)
        if cnt==display_number:
            print str(display_number) + ' Tweets Downloaded'
            display_number += DISPLAY_LIMIT
        if cnt==FILESIZE_LIMIT:
            cnt = 0
            tweets_file.close()
            display_number = DISPLAY_LIMIT
            rename(file_name,join(TEMP_PATH,'data'+str(file_number)+'.json')) #moving file to temp folder

            file_number+=1
            file_name = join(FILE_PATH,'data'+str(file_number)+'.json')
            tweets_file = open(file_name, "w")

        return True

    def on_error(self, status):
        print 'error: ' + status


if __name__ == '__main__':

    while True: #ensures continuous stream extraction
        try:
            #This handles Twitter authentication and the connection to Twitter Streaming API
           # print "sdadas"
            l = StdOutListener()
            auth = OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            stream = Stream(auth, l)

            #This line filter Twitter Streams to capture data by the top 20 most used keywords from the following URL:
                            # http://techland.time.com/2009/06/08/the-500-most-frequently-used-words-on-twitter/

            stream.filter(languages=["en"] , track=["a", "the", "i", "you", "to", "and", "is", "in", "u", "of", "it"])
        except:
            continue