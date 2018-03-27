#coding:utf8
import time

__author__ = 'chesian'
from scrapy.cmdline import execute




if __name__ == '__main__':
    execute('scrapy crawl broad'.split())

    # print time.strftime('%Y-%m-%d-%H',time.localtime())