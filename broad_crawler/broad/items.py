# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BroadItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    sources = scrapy.Field()

    title = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
    crawl_time = scrapy.Field()

    new_time = scrapy.Field()

    pre_size= scrapy.Field()  #
    size = scrapy.Field()

    # 锚文本
    anchor = scrapy.Field()
    # 父链接
    father_url = scrapy.Field()

    # 正文长度
    length = scrapy.Field()

    page_links_num = scrapy.Field()

