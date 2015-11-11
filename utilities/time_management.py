from datetime import datetime, timedelta, time
from time import sleep


def get_next_day(current_day):
    diff = timedelta(days=1)
    current_day += diff
    return current_day


def get_datetime(obj, time_string):
    set_time = datetime.strptime(time_string,'%H:%M')
    new_obj = obj.replace(hour = set_time.hour, minute = set_time.minute, second = 0)
    return new_obj


def get_today():
    return datetime.today()


def alarm(setTime):
    while True:
        if datetime.now()>=setTime:
            break
        remain = setTime - datetime.now()
        sleep(remain.seconds)
    print "Done"
