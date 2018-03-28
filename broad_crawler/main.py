#coding:utf8
import time
__author__ = 'chesian'
from broad.settings import WEB_SITE_NAME
from scrapy.cmdline import execute

if __name__ == '__main__':


    LOG_FILE_NAME = 'log/' + WEB_SITE_NAME + '-' + time.strftime("%Y-%m-%d-%H", time.localtime()) + '.log'
    execute(('scrapy crawl broad' + ' -s LOG_FILE=' + LOG_FILE_NAME).split())
    # print(LOG_FILE_NAME)
    # execute(('scrapy crawl broad').split())