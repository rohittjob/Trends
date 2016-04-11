"""

    Apply the LDA algorithm using libraries.
    Additional files if needed should be created.

    Ensure proper representation of generated topics.
    Also the fitted model should be reusable for tweet_segregation.py or just call segregation with the model as
    parameter.

    Experiment with number of topics. 5 should be good as we are talking about a single day.

"""
from os.path import join
from gensim import corpora, models

from utilities.os_util import get_dir
from utilities.constants import *
from utilities.time_management import start, stop, get_time
from utilities.config import NUMBER_OF_TOPICS

ROOT = get_dir(__file__)
DICTIONARY_PATH = join(ROOT, DATA_DIR, 'dict2.dict')
CORPUS_PATH = join(ROOT, DATA_DIR, 'corp.mm')

lda_params = {'num_topics': NUMBER_OF_TOPICS, 'passes': 20, 'alpha': 0.001}

corpus = corpora.MmCorpus(CORPUS_PATH)
dictionary = corpora.Dictionary.load(DICTIONARY_PATH)


print 'Started at ' + get_time() + '... '

start()

lda = models.LdaModel(corpus, id2word=dictionary,
                      num_topics=lda_params['num_topics'],
                      passes=lda_params['passes'],
                      alpha=lda_params['alpha'])

print lda.print_topics()

lda.save('data/lda2_2.lda')

stop()
