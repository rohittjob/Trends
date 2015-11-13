from engine.utilities.time_management import *
from engine.utilities.os_util import *
from engine.utilities.constants import *
from os.path import join
import subprocess
from multiprocessing import Process

TODAY = get_today()

ROOT = get_dir(__file__)
DAILY_SCRIPT_PATH = join(ROOT, DAILY_AGGREGATOR)
WEEKLY_SCRIPT_PATH = join(ROOT, WEEKLY_AGGREGATOR)


def daily_aggregation():
    print 'Starting Daily Aggregator... ',
    daily_aggregator = subprocess.Popen(['python', DAILY_SCRIPT_PATH], creationflags=subprocess.CREATE_NEW_CONSOLE)
    print 'Started with PID ' + str(daily_aggregator.pid)
    daily_aggregator.wait()


def weekly_aggregation():
    print 'Starting Weekly Aggregator... ',
    weekly_aggregator = subprocess.Popen(['python', WEEKLY_SCRIPT_PATH], creationflags=subprocess.CREATE_NEW_CONSOLE)
    print 'Started with PID ' + str(weekly_aggregator.pid)
    weekly_aggregator.wait()


if __name__ == '__main__':

    daily_aggregation()
    weekly_aggregation()
