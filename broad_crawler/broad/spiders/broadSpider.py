#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import os
import re
import sys 
import time
import scrapy

from scrapy_redis.spiders import RedisSpider, RedisCrawlSpider
from scrapy.http import Request, HtmlResponse
from scrapy.linkextractors import LinkExtractor
from broad.items import BroadItem


class BroadCrawlSpider(RedisCrawlSpider):
    name = "broadspider"
    # allowed_domains = ['finance.sina.com.cn']
    redis_key = "start_url"
    postfix = ""


    def parse(self, response):

        item = self.parse_page(response)
        yield item
        self.postfix = self.settings["POSTIFX"]
        # 添加URL
        urls = []
        link_extractor = LinkExtractor()
        if isinstance(response, HtmlResponse):

            links = link_extractor.extract_links(response)
            for link in links:
                if self.postfix in link.url:
                    urls.append(link.url)
        # print "urls", urls
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

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