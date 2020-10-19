#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'chesian'
__mtime__ = '2019/11/19'
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
import logging

logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
logging.info("start")

def parse_content(html, decoding, codeType):
    try:
        content = html.decode(decoding)
        return content
    except UnicodeDecodeError:
        codeType.__delitem__(codeType.index(decoding))
        if codeType.__len__() < 1:
            return None
        else:
            return parse_content(html, codeType[0], codeType)


def auto_decoding(html, decoding):
    codeType = ['utf-8', 'gb2312', ' gbk', 'utf8']
    return parse_content(html, decoding, codeType)

def dateConverter(str_time):
    # str_time = "2019年10月11日 01:59"
    # str_time = "10月11日 01:59"
    # str_time = "2019年10月11日"
    # str_time = "10月11日"
    # str_time = "2019-10-11 01:59"
    # str_time = "10-11 01:59saqw"
    import time
    formats = ['%m月%d日 %H:%M', '%Y年%m月%d日', '%m月%d日', '%Y-%m-%d %H:%M', '%Y-%m-%d %H:%M', '%m-%d %H:%M', '%Y/%m/%d', '%Y-%m-%d']
    r = ""
    for format in formats:
        try:
            news_time = time.strptime(str_time, format)
            r = time.strftime('%Y-%m-%d', news_time)
        except:
            pass
    return r





if __name__ == '__main__':

    if dateConverter("1992-23-23") is not None:
        print("ee")
