#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 17:52 
# @Author  : chesian
# @Site    : 
# @File    : MySpider.py
# @Software: PyCharm
import time
from scrapy import Request
from scrapy.http import HtmlResponse

from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisSpider

from broad_crawler.broad.items import BroadItem


class WebSpider(RedisSpider):
    name = 'webspider'
    redis_key = 'start_url'
    # allowed_domains = ['finance.sina.com.cn/']
    postfix = "finance.sina.com.cn"

    def parse(self, response):
        print "start parseing"
        link_extractor = LinkExtractor()
        if isinstance(response, HtmlResponse):
            links = link_extractor.extract_links(response)
            for link in links:
                if self.postfix in link.url:
                    links.append(link.url)

            for link in links:
                yield Request(link, callback=self.parse)

        #do_something_with_response
        page = BroadItem()
        content = response.body
        try:
            chatset = response.encoding
            content = content.decode(chatset, errors='ignore')
        except UnicodeDecodeError as e:
            print e
            raise UnicodeDecodeError
        page["content"] = content
        page['page_url'] = response.url
        page["title"] = response.xpath('//title/text()').extract()
        page['crawl_time'] = time.strftime('%Y-%m-%d-%H-%M',time.localtime())

        yield page

