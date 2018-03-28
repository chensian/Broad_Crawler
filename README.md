# Broad_Crawler
环境搭建教程
centos7安装redis
直接运行命令：yum install redis -y即可，安装完成后默认启动redis服务器, 安装完成后，redis默认是不能被远程连接的，此时
1、要修改配置文件/etc/redis.conf
#注释bind
# bind 127.0.0.1
# Redis默认不是以守护进程的方式运行，可以通过该配置项修改，设置为no
daemonize no
# 保护模式
protected-mode no
2、修改后，重启redis服务器
systemctl restart redis
在centos7环境下启动redis服务器的命令：systemctl start redis，启动客户端的命令：redis-cli，如果要增加redis的访问密码，修改配置文件/etc/redis.conf
#取消注释requirepass
requirepass redisredis  # redisredis就是密码（记得自己修改）
增加了密码后，启动客户端的命令变为：
redis-cli -a redisredis
3、测试是否能远程登陆
使用windows的命令窗口进入redis安装目录，用命令进行远程连接centos7的redis：
redis-cli -h yourip -p 6379
windows安装redis
下载地址：https://github.com/rgl/redis/downloads
or https://github.com/MicrosoftArchive/redis/releases

运行redis服务器的命令：安装目录下的redis-server.exe
运行redis客户端的命令：安装目录下的redis-cli.exe

安装部署scrapy-redis
github地址： https://github.com/darkrho/scrapy-redis

1、安装scrapy-redis命令（https://github.com/rolando/scrapy-redis）
pip install scrapy-redis
2、部署scrapy-redis
slave端：在windows上的settings.py文件的最后增加如下一行
REDIS_URL = 'redis://192.168.1.112:6379'
master端：在centos7上的settings.py文件的最后增加如下两行
REDIS_HOST = 'localhost'
REDIS_PORT = 6379


redis-cli -h 39.108.119.38 lpush start_url http://www.sina.com.cn/

反爬虫策略
动态设置user agent
禁用cookies
设置延迟下载
使用 Google cache
使用IP地址池（ Tor project 、VPN和代理IP）
使用 Crawlera

crawlera官方网址：http://scrapinghub.com/crawlera/
crawlera帮助文档：http://doc.scrapinghub.com/crawlera.html

1，注册一个crawlera账号并激活
2，登录网站获取App Key
3，激活crawlera这里注意一下，其实就是选择一个crawlera进行激活就好了，选择了最小的那个，进行完上面的操作就可以在程序里面加代码

1，安装scrapy-crawlera
pip install scrapy-crawlera
2，修改配置文件添加如下配置信息

DOWNLOADER_MIDDLEWARES = {
    'scrapy_crawlera.CrawleraMiddleware': 600
}
CRAWLERA_ENABLED = True
CRAWLERA_USER = '<API Key>'
CRAWLERA_PASS = 'crawlera的密码'

根据官方文档的提示，加入了如下的配置，保证了数据的正确获取,就我测试的观察，下面的配置，会使得程序能够自动的去获取数据，知道获取到正确的数据为止

CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS_PER_DOMAIN = 32
AUTOTHROTTLE_ENABLED = False
DOWNLOAD_TIMEOUT = 600

爬虫监控管理
windows 7 安装 scrapyd 
graphite 监控
JSON-RPC
https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/webservice.html



requeriment

scrapy
scrapy-redis
pymongo
