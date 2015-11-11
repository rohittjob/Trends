from utilities.time_management import *
from utilities.os_util import *
from utilities.constants import *
from os.path import join
from os import remove
from time import sleep
import subprocess
import psutil
from multiprocessing import Process, Value

TODAY = get_today()
STOP_TIME = None
RESTART_TIME = None

ROOT = get_dir(__file__)
EXTRACTOR_SCRIPT_PATH = join(ROOT,'Data Handler','extractor','tweet_extractor.py')
PREPROCESS_SCRIPT_PATH = join(ROOT,'Data Handler','processor','preprocess.py')


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
    EXTRACTOR_DATA_PATH = join(ROOT,'Data Handler','extractor','data')
    deleted = False
    while not deleted:
        try:
            files = get_files_in_dir(EXTRACTOR_DATA_PATH)

            for file in files:
                remove(join(EXTRACTOR_DATA_PATH,file))
            deleted = True
        except: None

    print 'Cleaned'



def data_extraction(extractor_pid):
    print 'Starting Extractor... ',
    extractor = subprocess.Popen(['python',EXTRACTOR_SCRIPT_PATH ])
    print 'Started with PID ' + str(extractor.pid)
    extractor_pid.value = extractor.pid
    extractor.wait()


def data_preprocess(stop):
    while stop.value == 0:
        print 'Starting Pre-processor... ',
        preprocessor = subprocess.Popen(['python',PREPROCESS_SCRIPT_PATH ])
        print 'Started with PID ' + str(preprocessor.pid)
        preprocessor.wait()
        print 'Sleeping'
        sleep(PREPROCESS_SLEEP_TIME)
        print 'Woke Up!!!'

if __name__ == '__main__':

    while True:  # run everyday
        STOP_TIME = get_datetime(TODAY,STOP_DATA_EXTRACTION_TIME)
        print STOP_TIME

        stop = Value('i', 0)
        extractor_pid = Value('i',0)

        extractor = Process(target=data_extraction, args=(extractor_pid, ))
        preprocessor = Process(target=data_preprocess, args=(stop, ))
        extractor.start()
        preprocessor.start()

        alarm(STOP_TIME)

        extractor.terminate()
        cleanup(extractor_pid.value)
        stop.value = 1
        print 'Waiting for preprocessor to exit... ',
        preprocessor.join()
        print 'Done'
        break

