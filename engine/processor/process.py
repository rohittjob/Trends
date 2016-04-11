"""

    Refer reference_files/process.py

    Does the same thing as previous process.py. So refer to that, only minor changes if necessary.
    Calls the preprocess.py and then calls entity_aggregation

"""

import subprocess

from os.path import join
from utilities.os_util import get_dir
from utilities.time_management import get_time
from utilities.constants import *

ROOT = get_dir(__file__)

PREPROCESS_SCRIPT_PATH = join(ROOT, PREPROCESSOR)
POSTPROCESS_SCRIPT_PATH = join(ROOT, ENTITY_AGGREGATOR)


def data_preprocess():
    print 'Starting Pre-processor... ',
    pre_processor = subprocess.Popen(['python', PREPROCESS_SCRIPT_PATH])
    print 'Started with PID ' + str(pre_processor.pid) + ' at ' + get_time()
    pre_processor.wait()


def data_postprocess():
    print 'Starting Post-processor... ',
    post_processor = subprocess.Popen(['python', POSTPROCESS_SCRIPT_PATH])
    print 'Started with PID ' + str(post_processor.pid) + ' at ' + get_time()
    post_processor.wait()


if __name__ == '__main__':
    data_preprocess()
    data_postprocess()


