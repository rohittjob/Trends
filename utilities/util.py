import time

start_time = None
end_time = None

############################## EXECUTION TIME FUNCTIONS #####################################

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
    start_time = time.time()


def stop():
    global end_time
    end_time = time.time()
    time_taken()


############################ PERCENTAGE COMPLETION FUNCTIONS #####################################

def check_percent(a,n,interval,prev): #a is the cur, n is total, it is the interval of display, prev is previouly displayed percentage
    if n == 0:
        return 0
    per = (a*100)/n
    rounded_per = (per/interval)*interval
    while prev < rounded_per:
        prev += interval
    print '\r',
    print str(prev) + '% complete',
    return prev



