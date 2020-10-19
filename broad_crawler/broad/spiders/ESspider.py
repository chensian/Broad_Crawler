#!/usr/bin/env python
# -*- encoding:utf-8 -*-
import codecs
import json
import bson
import scrapy
from scrapy.spiders import Spider

from broad.util.encodeUtil import auto_decoding, dateConverter


class ESSpider(Spider):
    name = "esspider"

    def start_requests(self):

        import time
        yield scrapy.Request('http://www.baidu.com/' + time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime()), self.parse)

    def parse(self, response):

        bson_file = codecs.open('E:/Jockjo/data/news_roll/emym_roll.bson', 'rb')

        # emym_normal emym_roll sina_roll tencent_hynews tencent_roll
        b = bson.decode_file_iter(bson_file)
        for index, item in enumerate(b):


            if index < 72221 :
                continue
            # # else:
            # #     print(index, item)
            # #     continue
            # if index > 7127:
            #     break

            # if index % 100 == 0:
            #     print(index)
            from bson.json_util import dumps
            if "url" not in item:
                item['url'] = item['_id']
            del item['_id']
            # item["document"]
            # print(str(item["document"],'utf-8'))
            item["document"] = auto_decoding(item["document"], "utf8")
            item["title"] = item["title"].strip()
            item["news_time"] = item["news_time"].strip()
            item = json.loads(dumps(item))
            item["news_time"] = dateConverter(item["news_time"])
            # try:
            #     if "1900" in item["news_time"]:
            #         year = item["url"].split("/")[-1].split(",")[1][0:4]
            #         item["news_time"] = item["news_time"].replace("1900", year)
            # except:
            #     print(item["news_time"])


            yield item

