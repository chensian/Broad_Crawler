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
from broad_crawler.broad.items import BroadItem



class BroadCrawlSpider(RedisSpider):
    name = "broad"
    redis_key = "start_url"
    postfix = ""

    def parse(self, response):

        item = self.parse_page(response)
        yield item

        # 添加URL
        links = []
        link_extractor = LinkExtractor()
        if isinstance(response, HtmlResponse):
            links = link_extractor.extract_links(response)
            for link in links:
                if self.postfix in link.url:
                    links.append(link.url)
        for link in links:
            yield scrapy.Request(link, callback=self.parse)

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
        item["title"] = response.xpath('//title/text()').extract()
        item['page_url'] = response.url
        item['crawl_time'] = time.strftime('%Y-%m-%d-%H-%M',time.localtime())

        return item