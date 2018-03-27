#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 17:52 
# @Author  : chesian
# @Site    : 
# @File    : MySpider.py
# @Software: PyCharm
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider

from broad_crawler.broad.items import BroadItem


class PageSpider(RedisCrawlSpider):
    name = 'pagespider'
    redis_key = 'pagespider:start_urls'
    allowed_domains = ['finance.sina.com.cn/']

    rules = [
        Rule(SgmlLinkExtractor(), callback='parse_item',follow=True),
    ]

    def parse_item(self, response):
        print "start parsing"
        #do_something_with_response
        broad = BroadItem()
        content = response.body
        try:
            chatset = response.encoding
            content = content.decode(chatset, errors='ignore')
        except UnicodeDecodeError as e:
            print e
            raise UnicodeDecodeError
        broad["content"] = content
        broad['page_url'] = response.url
        broad["title"] = response.xpath('//title/text()').extract()

        yield page

