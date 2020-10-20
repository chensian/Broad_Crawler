# -*- coding: utf-8 -*-

# Scrapy settings for broad project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'broad'

SPIDER_MODULES = ['broad.spiders']
NEWSPIDER_MODULE = 'broad.spiders'

# Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# REDIS_HOST = '192.168.5.203'
# REDIS_PORT = 6379
REDIS_URL = 'redis://192.168.5.203:6379'

FILTER_URL = 'redis://192.168.5.203:6379'
# FILTER_HOST = 'localhost'
# FILTER_PORT = 6379

"""
    这是去重队列的Redis信息。
    原先的REDIS_HOST、REDIS_PORT只负责种子队列；由此种子队列和去重队列可以分布在不同的机器上。
"""

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
DOWNLOAD_HANDLERS = {'S3': None,}

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 100

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)COOKIES_ENABLED = False
#COOKIES_ENABLED = False
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'broad.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html

DOWNLOADER_MIDDLEWARES = {
    # 'broad.middlewares.MyCustomDownloaderMiddleware': 543,
    'broad.middleware.UserAgentMiddleware': 200,
}


# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    #    'broad.pipelines.MySQLStorePipeline': 300,
    #     'broad.pipelines.SQLiteStorePipeline': 300,
    #     'scrapy_redis.pipelines.RedisPipeline': 300,
    # 'broad.pipelines.BroadPipeline': 300,
    #    'broad.pipelines.BroadImagesPipeline': 400,
    #    'scrapy.pipelines.images.ImagesPipeline': 1,
    "broad.pipelines.MongoDBPipeline": 403,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Broad Crawl Setting
CONCURRENT_REQUESTS = 100
REACTOR_THREADPOOL_MEAXSIZE = 20
LOG_LEVEL = 'INFO'
COOKIES_ENABLED = False
RETRY_ENABLED = False
DOWNLOAD_TIMEOUT = 15
# REDIRECT_ENABLED = False
AJAXCRAWL_ENABLED = True




# project customs setting

#!/usr/bin/env bash
# redis-cli -h 192.168.5.203  -n 2 lpush start_url https://finance.sina.com.cn
# start_url
# https://www.itjuzi.com/         1
# https://finance.sina.com.cn     2
# https://finance.yahoo.com/      3
# http://www.eastmoney.com/    4
# https://xueqiu.com/         5
# http://www.p5w.net/          6


REDIS_PARAMS = {
    # 'password' : 'xxxxxx',
    #  'db': 1
    'db': 2
    #  'db': 3
    #  'db': 4
    #  'db': 6
}
FILTER_DB = 2

# POSTIFX = 'itjuzi.com'
POSTIFX = 'finance.sina.com.cn'
# POSTIFX = 'guba.sina.com.cn'
# POSTIFX = 'finance.yahoo.com'
# POSTIFX = 'eastmoney.com'
# POSTIFX = 'p5w.net'

# MONGO_DB_NAME = 'ITJUZI'
MONGO_DB_NAME = 'SINA'
# MONGO_DB_NAME = 'SINA_GUBA'
# MONGO_DB_NAME = 'YAHOO'
# MONGO_DB_NAME = 'EASTMONEY'
# MONGO_DB_NAME = 'P5W'