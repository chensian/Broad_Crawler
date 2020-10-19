#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import scrapy
import time
from pyquery import PyQuery as pq
from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider

from broad.items import BroadItem
from broad.util.date_extract import extract_date
from broad.util.encodeUtil import dateConverter, auto_decoding
from main import cx


class BroadCrawlSpider(RedisCrawlSpider):
    name = "broadspider2"
    # allowed_domains = ['finance.sina.com.cn']
    redis_key = "start_url"
    postfix = ""

    def parse(self, response):

        url = response.url

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
                    urls.append([link.url, link.text])
        # print "urls", urls
        for url, anchor in urls:
            # 加入URL评分器
            # if self.settings["IS_URL_ORDER"]:
            #
            #     #####
            #     #####
            #     #####
            #     #####
            #     #####
            #
            #     priority_score = 1
            # else:
            #     priority_score = 0
            yield scrapy.Request(url, meta={"anchor": anchor, "father_url": response.url}, callback=self.parse, priority=1)

    def parse_page(self, response):

        anchor = ""
        if "anchor" in response.meta:
            anchor =response.meta["anchor"]

        father_url = ""
        if "father_url" in response.meta:
            father_url =response.meta["father_url"]

        item = BroadItem()
        content = auto_decoding(response.body, "utf8")
        item['new_time'] = extract_date(content)
        if item['new_time'] is None:
            return None

        item["title"] = response.xpath('//title/text()').extract_first()
        item['url'] = response.url

        item['anchor'] =anchor
        item['father_url'] =father_url

        # filter js  css

        content = pq(content)
        item["pre_size"] = len(content.html())
        item["sources"] = content.remove('script').remove('style').remove('link').html()
        item["size"] = len(content.html())
        a_links = content("a")
        item["page_links_num"] = len(a_links)

        # # 抽取出正文
        try:
            content = cx.filter_tags(content.html())
            content = cx.getText(content)
        except Exception as e:
            print(e)
            print(response.url, "cx ERROR")
        item["content"] = content
        item["length"] = len(content)

        item['crawl_time'] = time.strftime('%Y-%m-%d-%H-%M',time.localtime())

        # print(item['new_time'])

        return item