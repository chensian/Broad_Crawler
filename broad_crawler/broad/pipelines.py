#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 17:52
# @Author  : chesian
# @Site    :
# @File    : MySpider.py
# @Software: PyCharm

import pymongo
import time

from broad_crawler.broad.items import BroadItem


class BroadSpiderPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoDBPipeline(object):
    def __init__(self):
        clinet = pymongo.MongoClient("localhost", 27017)
        self.db = clinet["Broad"]

    def process_item(self, item, spider):
        """ 判断item的类型，并作相应的处理，再入数据库 """
        if isinstance(item, BroadItem):
            try:
                self.db[time.strftime('%Y-%m-%d',time.localtime())].insert(dict(item))
            except Exception:
                pass



