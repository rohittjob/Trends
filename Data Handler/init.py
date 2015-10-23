import os
from utilities import mongo
ROOT = os.path.dirname(os.path.realpath(__file__))
ROOT = os.path.dirname(ROOT)

# BATCH_FILE = os.path.join(ROOT,'start_mongo.bat')
# os.system(BATCH_FILE)


PYTHON_PACKAGES = ['os','json','tweepy','pymongo']
missing_python_packages = []
flag = True


def check(package):
    global flag
    try:
        __import__(package)
    except:
        missing_python_packages.append(package)
        flag = False


def check_dependencies():
    print "Checking dependencies... ",

    for package in PYTHON_PACKAGES:
        check(package)

    if flag:
        print "SUCCESS"
        return True

    else:
        print "FAILURE"
        print
        print "The following python packages are missing from your system:"
        for package in missing_python_packages:
            print package

        print
        print "Install these packages and run this script again"
        return False

if __name__ == '__main__':
    if check_dependencies():
        mongo.init()
