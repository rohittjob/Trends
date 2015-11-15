from datetime import datetime, timedelta
from time import sleep, time


def get_next_day(current_day):
    diff = timedelta(days=1)
    current_day += diff
    return current_day


def get_datetime_from_string(obj, time_string):
    set_time = datetime.strptime(time_string, '%H:%M')
    new_obj = obj.replace(hour=set_time.hour, minute=set_time.minute, second=0)
    return new_obj


def get_now():
    return datetime.now()


def get_today():
    return datetime.today()


def get_time():
    return datetime.now().time().strftime('%H:%M:%S')


def add_seconds_to_datetime(obj, seconds):
    return obj + timedelta(seconds=seconds)


def alarm(proc_name, set_time):
    print "Alarm set for '" + proc_name + "' at " + str(set_time)
    while True:
        if datetime.now() >= set_time:
            break
        remain = set_time - datetime.now()
        sleep(remain.seconds)
    print "Alarm Rings..."


def get_date_string(date_obj):
    date_string = date_obj.strftime('%d-%m-%Y')
    return date_string


# %%%%%%%%%%%%%%%%%%%%%%%%% EXECUTION TIME FUNCTIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


start_time = None
end_time = None


def time_taken():
    global start_time, end_time
    seconds = end_time - start_time
    minutes = seconds/60
    hours = int(minutes/60)
    minutes = int(minutes - hours*60)
    seconds = int(seconds - minutes*60 - hours*60*60)

    print 'Time to execute = ' + str(hours) + ':' + str(minutes) + ':' + str(seconds)


def start():
    global start_time
    start_time = time()


def stop():
    global end_time
    end_time = time()
    time_taken()
