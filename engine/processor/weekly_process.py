import subprocess

from utilities.os_util import *
from utilities.time_management import get_time
from utilities.constants import *

ROOT = get_dir(__file__)


WEEKLY_AGGREGATOR_SCRIPT_PATH = join(ROOT, WEEKLY_AGGREGATOR)
TRENDS_EXTRACTOR_SCRIPT_PATH = join(ROOT, TRENDS_EXTRACTOR)
GRAPH_APPROXIMATOR_SCRIPT_PATH = join(ROOT, GRAPH_APPROXIMATOR)


def weekly_aggregation():
    print 'Starting Weekly Aggregator... ',
    weekly_aggregator = subprocess.Popen(['python', WEEKLY_AGGREGATOR_SCRIPT_PATH])
    print 'Started with PID ' + str(weekly_aggregator.pid) + ' at ' + get_time()
    weekly_aggregator.wait()


def trends_extraction():
    print 'Starting Trends Extractor... ',
    trends_extractor = subprocess.Popen(['python', TRENDS_EXTRACTOR_SCRIPT_PATH])
    print 'Started with PID ' + str(trends_extractor.pid) + ' at ' + get_time()
    trends_extractor.wait()


def graph_approximation():
    print 'Starting Graph Approximator... ',
    graph_approximator = subprocess.Popen(['python', GRAPH_APPROXIMATOR_SCRIPT_PATH])
    print 'Started with PID ' + str(graph_approximator.pid) + ' at ' + get_time()
    graph_approximator.wait()


if __name__ == '__main__':
    weekly_aggregation()
    trends_extraction()
    graph_approximation()

