#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'chesian'
__mtime__ = '2019/10/4'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from newspaper import Article

url = 'https://mp.weixin.qq.com/s?src=11&timestamp=1570192201&ver=1892&signature=EaoEcECdjDUOZRXYxpxzOKWNiRQsyCpHEWC-t9pkwaV2Xibr17cKRnZvPJ' \
      '76ae5jPCwlzqpPzVTaEcZmyugh4XXBLrPARIHmQlnvYtjLe6OGvG*QEfKXWcJg*cJpd2gX&new=1'
article = Article(url)
article.download()

# print(article.html)

article.parse()

print(article.authors)

print(article.publish_date)
# datetime.datetime(2013, 12, 30, 0, 0)
#
# article.text
# 'Washington (CNN) -- Not everyone subscribes to a New Year's resolution...'
#
# article.top_image
# 'http://someCDN.com/blah/blah/blah/file.png'
#
# article.movies
# ['http://youtube.com/path/to/link.com', ...]
# article.nlp()
#
# article.keywords
# ['New Years', 'resolution', ...]
#
# article.summary
# 'The study shows that 93% of people ...'
# import newspaper
#
# cnn_paper = newspaper.build('http://cnn.com')
#
# for article in cnn_paper.articles:
# >>>     print(article.url)
# http://www.cnn.com/2013/11/27/justice/tucson-arizona-captive-girls/
# http://www.cnn.com/2013/12/11/us/texas-teen-dwi-wreck/index.html
# ...
#
# for category in cnn_paper.category_urls():
# >>>     print(category)
#
# http://lifestyle.cnn.com
# http://cnn.com/world
# http://tech.cnn.com
# ...
#
# cnn_article = cnn_paper.articles[0]
# cnn_article.download()
# cnn_article.parse()
# cnn_article.nlp()
# ...
# from newspaper import fulltext
#
# html = requests.get(...).text
# text = fulltext(html)
# Newspaper can extract and detect languages seamlessly. If no language is specified, Newspaper will attempt to auto detect a language.
#
# from newspaper import Article
# url = 'http://www.bbc.co.uk/zhongwen/simp/chinese_news/2012/12/121210_hongkong_politics.shtml'
#
# a = Article(url, language='zh') # Chinese
#
# a.download()
# a.parse()
#
# print(a.text[:150])
# 香港行政长官梁振英在各方压力下就其大宅的违章建
# 筑（僭建）问题到立法会接受质询，并向香港民众道歉。
# 梁振英在星期二（12月10日）的答问大会开始之际
# 在其演说中道歉，但强调他在违章建筑问题上没有隐瞒的
# 意图和动机。 一些亲北京阵营议员欢迎梁振英道歉，
# 且认为应能获得香港民众接受，但这些议员也质问梁振英有
#
# print(a.title)
# 港特首梁振英就住宅违建事件道歉
# If you are certain that an entire news source is in one language, go ahead and use the same api :)
#
# import newspaper
# sina_paper = newspaper.build('http://www.sina.com.cn/', language='zh')
#
# for category in sina_paper.category_urls():
# >>>     print(category)
# http://health.sina.com.cn
# http://eladies.sina.com.cn
# http://english.sina.com
# ...
#
# article = sina_paper.articles[0]
# article.download()
# article.parse()
#
# print(article.text)
#
# print(article.title)
