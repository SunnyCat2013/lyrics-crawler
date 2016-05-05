import math
import string
import sys
from datetime import datetime
from os import path, mkdir
from threading import Thread
from time import time
from urllib import request

usage = "python hindilyrics-crawler <crawl type - full/incr> <destination>"
start_address = 'http://www.hindilyrics.net'


def print_info(level, message):
    message = '(' + datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S') + ') INFO: ' + message
    for i in range(0, level):
        message = '\t' + message
    print(message)


def download_movie(url):
    pass


def download_movies_from_page(level, init, number):
    global start_address
    print_info(level, 'Started thread for downloading movies starting with {0} page {1}'.format(init, number))

    website = start_address + '/lyrics/hindi-songs-starting-{0}-page-{1}.html'.format(init, number)
    raw_html = str(request.urlopen(website).read())



    pass


def initial(level, init):
    global start_address
    print_info(level, 'Started thread for downloading metadata for movies starting with {0}'.format(init))
    website = start_address + '/lyrics/hindi-songs-starting-{0}-page-1.html'.format(init)

    raw_html = str(request.urlopen(website).read())
    number_of_movies = raw_html.count('<li>')

    print_info(level, 'Found {0} movies starting with {1}.'.format(number_of_movies, init))

    number_of_pages = math.ceil(number_of_movies / 90.0)

    threads = {}
    for i in range(1, number_of_pages + 1):
        threads[i] = Thread(target=download_movies_from_page, args=(level + 1, init, i))
        threads[i].start()


def full_crawl(level=0):
    initials = ['0'] + string.ascii_lowercase

    while True:
        print_info(level, 'Starting full crawl')
        thread_dict = {}

        for init in initials:
            thread_dict[init] = Thread(target=initial, args=(level + 1, init))
            thread_dict[init].start()

        for init in initials:
            thread_dict[init].join()


def incremental_crawl():
    pass


def main():
    if len(sys.argv) != 3:
        print(usage)
        raise ValueError('Expected {0} arguments recieved {1}.'.format(3, len(sys.argv)))

    crawl_type = sys.argv[1]

    if crawl_type not in ('full', 'incr'):
        raise ValueError('Invalid crawl type')

    if not path.isdir(sys.argv[2]):
        mkdir(sys.argv[2])

    if crawl_type.matches('full'):
        full_crawl(0)
    else:
        incremental_crawl()


if __name__ == "__main__":
    main()
