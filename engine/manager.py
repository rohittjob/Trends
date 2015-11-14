import subprocess
from multiprocessing import Process, Value
from engine.utilities.time_management import *
from engine.utilities.os_util import *
from engine.utilities.constants import *
from engine.utilities.config import *
from os import remove

TODAY = get_today()
TOMORROW = get_next_day(TODAY)
STOP_TIME = None
RESTART_TIME = None

ROOT = get_dir(__file__)

EXTRACTOR_SCRIPT_PATH = join(ROOT, EXTRACTOR_DIR, EXTRACTOR)
PREPROCESS_SCRIPT_PATH = join(ROOT, PROCESSOR_DIR, PREPROCESSOR)
POSTPROCESS_SCRIPT_PATH = join(ROOT, PROCESSOR_DIR, POSTPROCESSOR)
EXTRACTOR_DATA_PATH = join(ROOT, EXTRACTOR_DIR, EXTRACTOR_DATA_DIR)


def cleanup():

    print 'Cleaning up breadcrumbs... ',
    deleted = False
    while not deleted:
        try:
            data_files = get_files_in_dir(EXTRACTOR_DATA_PATH, JSON)

            for data_file in data_files:
                remove(join(EXTRACTOR_DATA_PATH, data_file))
            deleted = True

        except: None

    print 'Cleaned'


def data_extraction():
    print 'Starting Extractor... ',
    extractor = subprocess.Popen(['python', EXTRACTOR_SCRIPT_PATH], creationflags=subprocess.CREATE_NEW_CONSOLE)
    print 'Started with PID ' + str(extractor.pid)
    return extractor


def data_preprocess(stop_bool):
    while stop_bool.value == 0:
        print 'Starting Pre-processor... ',
        pre_processor = subprocess.Popen(['python', PREPROCESS_SCRIPT_PATH])
        print 'Started with PID ' + str(pre_processor.pid)
        pre_processor.wait()
        print 'Pre-processor Sleeping'
        sleep(PREPROCESS_SLEEP_TIME)
        print 'Pre-processor Woke Up!!!'


def data_postprocess():
    print 'Starting Post-processor... ',
    post_processor = subprocess.Popen(['python', POSTPROCESS_SCRIPT_PATH], creationflags=subprocess.CREATE_NEW_CONSOLE)
    print 'Started with PID ' + str(post_processor.pid)


if __name__ == '__main__':
    while True:  # run everyday
        STOP_TIME = get_datetime_from_string(TODAY, STOP_DATA_EXTRACTION_TIME)
        RESTART_TIME = get_datetime_from_string(TOMORROW, RESTART_DATA_EXTRACTION_TIME)

        stop_preprocessor = Value('i', 0)
        extractor_pid = Value('i', 0)

        extractor = data_extraction()
        preprocessor = Process(target=data_preprocess, args=(stop_preprocessor,))

        preprocessor.start()

        alarm(STOP_TIME)

        extractor.terminate()
        cleanup()

        stop_preprocessor.value = 1
        preprocessor.join()
        print 'Pre-processor exiting...'

        data_postprocess()

        alarm(RESTART_TIME)
        print 'Restarting scripts!!! '
        TODAY = TOMORROW
        TOMORROW = get_next_day(TODAY)

