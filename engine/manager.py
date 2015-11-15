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
EXTRACTOR_DATA_PATH = join(ROOT, EXTRACTOR_DIR, EXTRACTOR_DATA_DIR)
PROCESS_SCRIPT_PATH = join(ROOT, PROCESSOR_DIR, PROCESSOR)
WEEKLY_PROCESS_SCRIPT_PATH = join(ROOT, PROCESSOR_DIR, WEEKLY_AGGREGATOR)


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


def data_processing(stop_bool, stop_time):

    next_stop = get_now()
    while stop_bool.value == 0:
        next_stop = min(add_seconds_to_datetime(next_stop, PROCESSOR_SLEEP_TIME), stop_time)
        print 'Processor started sleeping at ' + get_time()
        alarm(PROCESSOR_PROCESS, next_stop)
        print 'Processor Woke Up!!!'
        print 'Starting Processor... ',
        processor = subprocess.Popen(['python', PROCESS_SCRIPT_PATH])
        print 'Started with PID ' + str(processor.pid)
        processor.wait()


def data_weekly_process():
    print 'Starting Weekly Processor... ',
    weekly_processor = subprocess.Popen(['python', WEEKLY_PROCESS_SCRIPT_PATH])
    print 'Started with PID ' + str(weekly_processor.pid)


if __name__ == '__main__':
    while True:  # run everyday
        STOP_TIME = get_datetime_from_string(TODAY, STOP_DATA_EXTRACTION_TIME)
        RESTART_TIME = get_datetime_from_string(TOMORROW, RESTART_DATA_EXTRACTION_TIME)

        stop_processor = Value('i', 0)
        extractor_pid = Value('i', 0)

        extractor = data_extraction()
        processor = Process(target=data_processing, args=(stop_processor, STOP_TIME,))

        processor.start()

        alarm(MANAGER, STOP_TIME)

        extractor.terminate()
        cleanup()

        stop_processor.value = 1
        processor.join()
        print 'Processor exiting...'

        data_weekly_process()

        alarm(MANAGER, RESTART_TIME)
        print 'Restarting scripts!!! '
        TODAY = TOMORROW
        TOMORROW = get_next_day(TODAY)

