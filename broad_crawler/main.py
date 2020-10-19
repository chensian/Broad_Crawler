#coding:utf8
import codecs
import time


from bs4 import BeautifulSoup

from broad.util.cx_extractor import CxExtractor

__author__ = 'chesian'
from broad.settings import MONGO_DB_NAME
from scrapy.cmdline import execute

cx = CxExtractor()

if __name__ == '__main__':

    spider_name = "broadspider2"
    LOG_FILE_NAME = 'log/' + MONGO_DB_NAME + '-' + time.strftime("%Y-%m-%d-%H", time.localtime()) + '.log'
    execute(('scrapy crawl ' + spider_name +  ' -s LOG_FILE=' + LOG_FILE_NAME).split())
    # execute(('scrapy crawl ' + spider_name).split())
    # print(LOG_FILE_NAME)
    # execute(('scrapy crawl broad').split())
