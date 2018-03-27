#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import os
import re
import sys 
import time
import scrapy
from bs4 import BeautifulSoup

from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request, HtmlResponse
from scrapy.linkextractors import LinkExtractor
from scrapy.utils.project import get_project_settings
from broad_crawler.broad.items import BroadItem
reload(sys)
sys.setdefaultencoding('utf-8')


class BroadCrawlSpider(RedisSpider):
    name = "broad"
    redis_key = "start_url"
    postfix = ""

    def __init__(self):
        settings = get_project_settings()
        self.__class__.postfix = settings.get('POSTFIX')

    def parse(self, response):

        item = self.parse_page(response)
        yield item

        # 添加URL
        links = self.extractLinks(response)
        for link in links:
            yield scrapy.Request(link, callback=self.parse)


    def extractLinks(self, response):
        '''
        抽取url
        :param response:
        :return:
        '''
        retv = []
        link_extractor = LinkExtractor()
        if isinstance(response, HtmlResponse):
            links = link_extractor.extract_links(response)
            for link in links:
                if self.postfix in link.url:
                    retv.append(link.url)
        return retv

    def parse_page(self, response):
        item = BroadItem()
        content = response.body
        try:
            chatset = response.encoding
            content = content.decode(chatset, errors='ignore')
        except UnicodeDecodeError as e:
            print e
            raise UnicodeDecodeError
        item["content"] = content
        title = response.xpath('//title/text()').extract()
        if len(title) > 0:
            item['title'] = ''.join(title[0].replace('|', ','). \
                                    replace('\"', '').replace('\'', ''). \
                                    replace('(', '[').replace(')', ']'). \
                                    replace('#', '').split())
        else:
            item['title'] = ''
        item['page_url'] = response.url
        return item