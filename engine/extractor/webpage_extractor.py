'''

    Given the URLs generated in info_generator/related_links.py,
    extract the corresponding webpage for further analysis.
    Clean to the maximum extent.
    Need not save in HTML format, can be beautiful souped or any other efficient HTML representations.
    Choose efficient storage like Mongo or pickle to save the final output.

    Can save the original HTML just in case. Save it in a separate folder.

'''
import urllib
from os.path import join

from utilities.os_util import get_dir
from utilities.constants import *

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = { 'User-Agent' : user_agent }

ENGINE_ROOT = get_dir(get_dir(__file__))
URL_DIR = join(ENGINE_ROOT, INFO_GENERATOR_DIR, TSV_DIR)
HTML_PATH = join(ENGINE_ROOT, INFO_GENERATOR_DIR, HTML_DIR)


def get_urls(topic_id):
    urls = []
    file_path = join(URL_DIR, 'topic' + str(topic_id) + TSV)
    f = open(file_path)

    for url in f:
        urls.append(url)

    return urls


def execute():
    urls = get_urls(2)  # TODO for all topics
    for url_id, url in enumerate(urls):
        html_file = join(HTML_PATH, 'topic2_' + str(url_id) + HTML)
        urllib.urlretrieve(url, html_file)


if __name__ == '__main__':
    execute()


