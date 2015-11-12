from utilities.time_management import *
from utilities.os_util import *
from utilities.constants import *
from utilities.config import *
from os.path import join
from os import remove
from time import sleep
import subprocess
import psutil
from multiprocessing import Process, Value

TODAY = get_today()
TOMORROW = get_next_day(TODAY)
STOP_TIME = None
RESTART_TIME = None

ROOT = get_dir(__file__)

EXTRACTOR_SCRIPT_PATH = join(ROOT, DATA_HANDLER_DIR, EXTRACTOR_DIR, EXTRACTOR)
PREPROCESS_SCRIPT_PATH = join(ROOT, DATA_HANDLER_DIR, PROCESSOR_DIR, PREPROCESSOR)
POSTPROCESS_SCRIPT_PATH = join(ROOT, DATA_HANDLER_DIR, PROCESSOR_DIR, POSTPROCESSOR)
EXTRACTOR_DATA_PATH = join(ROOT, DATA_HANDLER_DIR, EXTRACTOR_DIR, EXTRACTOR_DATA_DIR)


def cleanup(extractor_pid):
    print 'Cleaning up after extractor... '
    print 'Killing extractor process PID ' + str(extractor_pid) + '... ',

    while True:
        try:
            p = psutil.Process(extractor_pid)
            p.terminate()
        except:  # break when NoSuchProcess exception is raised
            break
    print 'Killed!!'

    print 'Cleaning up breadcrumbs... ',
    deleted = False
    while not deleted:
        try:
            data_files = get_files_in_dir(EXTRACTOR_DATA_PATH, JSON)

            for data_file in data_files:
                remove(join(EXTRACTOR_DATA_PATH, data_file))
            deleted = True
        except:
            None

    print 'Cleaned'


def data_extraction(extractor_pid):
    print 'Starting Extractor... ',
    extractor = subprocess.Popen(['python', EXTRACTOR_SCRIPT_PATH])
    print 'Started with PID ' + str(extractor.pid)
    extractor_pid.value = extractor.pid
    extractor.wait()


def data_preprocess(stop):
    while stop.value == 0:
        print 'Starting Pre-processor... ',
        pre_processor = subprocess.Popen(['python', PREPROCESS_SCRIPT_PATH])
        print 'Started with PID ' + str(pre_processor.pid)
        pre_processor.wait()
        print 'Sleeping'
        sleep(PREPROCESS_SLEEP_TIME)
        print 'Woke Up!!!'


def data_postprocess():
    print 'Starting Post-processor... ',
    post_processor = subprocess.Popen(['python', POSTPROCESS_SCRIPT_PATH])
    print 'Started with PID ' + str(post_processor.pid)
    post_processor.wait()


if __name__ == '__main__':

    while True:  # run everyday
        STOP_TIME = get_datetime(TODAY, STOP_DATA_EXTRACTION_TIME)
        RESTART_TIME = get_datetime(TOMORROW, RESTART_DATA_EXTRACTION_TIME)

        stop_preprocessor = Value('i', 0)
        extractor_pid = Value('i', 0)

        extractor = Process(target=data_extraction, args=(extractor_pid,))
        preprocessor = Process(target=data_preprocess, args=(stop_preprocessor,))
        extractor.start()
        preprocessor.start()

        alarm(STOP_TIME)

        extractor.terminate()
        cleanup(extractor_pid.value)

        print 'Waiting for preprocessor to exit... ',
        stop_preprocessor.value = 1
        preprocessor.join()
        print 'Done'

        postprocessor = Process(target=data_postprocess)
        postprocessor.start()

        alarm(RESTART_TIME)
        print 'Restarting scripts!!! '
        TODAY = TOMORROW
        TOMORROW = get_next_day(TODAY)

