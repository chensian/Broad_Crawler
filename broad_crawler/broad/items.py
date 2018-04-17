# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BroadItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    _id = scrapy.Field()
    content = scrapy.Field()
    crawl_time = scrapy.Field()

    pre_size= scrapy.Field()  #
    size = scrapy.Field()

