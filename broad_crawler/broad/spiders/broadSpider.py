#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import time

import newspaper
import scrapy
from bs4 import BeautifulSoup

from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor

from broad.items import BroadItem
from broad.util.date_extract import extract_date
from broad.util.encodeUtil import dateConverter


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
        # print("urls", urls)
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse_page(self, response):

        print(response.url)

        item = BroadItem()
        content = response.body
        try:
            chatset = response.encoding
            content = content.decode(chatset, errors='ignore')
        except UnicodeDecodeError as e:
            print("ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", response.url)
            raise UnicodeDecodeError

        item["title"] = response.xpath('//title/text()').extract()
        item['url'] = response.url

        # filter js  css
        soup = BeautifulSoup(content, "lxml")
        # item['pre_size'] = len(soup.text)
        # for s in soup('script'):
        #     # print s
        #     s.extract()
        # for s in soup('style'):
        #     # print s
        #     s.extract()
        # item['size'] = len(soup.text)
        item["content"] = soup.decode_contents(formatter="html")

        item['new_time'] = dateConverter(extract_date(content))
        item['crawl_time'] = time.strftime('%Y-%m-%d-%H-%M',time.localtime())

        return item