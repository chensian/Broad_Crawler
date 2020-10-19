#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'chesian'
__mtime__ = '2019/9/5'
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

# Elasticsearch 基本介绍及其与 Python 的对接实现
#  https://cuiqingcai.com/6214.html
import codecs
import json
import logging
import pprint

import bson

from broad.util.encodeUtil import auto_decoding, dateConverter

logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
logging.info("start")



from elasticsearch6 import Elasticsearch, helpers






def createIndex():
    # es = Elasticsearch()
    result = es.indices.create(index='news', ignore=400)
    print(result)



# data = {'title': '美国留给伊拉克的是个烂摊子吗', 'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm'}
# data = {'title': '习近平向第四届中国-阿拉伯国家博览会致贺信', 'url': 'https://new.qq.com/omn/20190905/20190905A078JM00.html',
#         'content':'新华社北京9月5日电 第四届中国－阿拉伯国家博览会9月5日在宁夏银川开幕。国家主席习近平致贺信，对会议的召开表示热烈祝贺。习近平指出，近年来，中阿双方顺应时代潮流和各自发展需要，携手推动共建“'
#                   '一带一路”，取得了丰硕成果。习近平强调，去年7月，我在中阿合作论坛第八届部长级会议开幕式上宣布建立全面合作、共同发展、面向未来的中阿战略伙伴关系。本届博览会为双方深化务实合作、'
#                   '推动共建“一带一路”高质量发展搭建了有益平台。希望双方以此为契机，抓住机遇，开拓路径，挖掘潜力，携手推动中阿战略伙伴关系实现更大发展，更好造福中阿双方人民。'}

# data = {'title': '关于发扬斗争精神，习近平这样告诫全党', 'url': 'https://new.qq.com/rain/a/20190905A08YEV00',
#         'content':'9月3日，习近平总书记在2019年秋季学期中央党校（国家行政学院）中青年干部培训班开班式上发表重要讲话强调，广大干部特别是年轻干部要经受严格的思想淬炼、政治历练、实践锻炼，发扬斗争精神，增强斗争本领，'
#                   '为实现“两个一百年”奋斗目标、实现中华民族伟大复兴的中国梦而顽强奋斗。面对当今世界百年未有之大变局，习近平总书记深刻总结马克思主义产生和发展、社会主义国家诞生和发展的斗争历程，深刻总结我们党在斗争'
#                   '中诞生、在斗争中发展、在斗争中壮大的恢弘实践，深刻阐明了新时代的干部发扬斗争精神、增强斗争本领的重大意义，从坚定斗争意志、把准斗争方向、明确斗争任务、掌握斗争规律、讲求斗争方法等方面，科学回答了'
#                   '新时代的干部发扬斗争精神、增强斗争本领的重大理论和实践问题。'}

data = {'title': '中美经贸高级别磋商双方牵头人通话 将于9月中旬开展认真磋商', 'url': 'https://new.qq.com/omn/FIN20190/FIN2019090500201200.html',
        'content':'双方同意10月初在华盛顿举行第十三轮中美经贸高级别磋商，此前双方将保持密切沟通，工作层将于9月中旬开展认真磋商，为高级别磋商取得实质性进展做好充分准备。'
                  '9月5日上午，中共中央政治局委员、国务院副总理、中美全面经济对话中方牵头人刘鹤应约与美国贸易代表莱特希泽、财政部长姆努钦通话。双方同意10月初在华盛顿举行第'
                  '十三轮中美经贸高级别磋商，此前双方将保持密切沟通，工作层将于9月中旬开展认真磋商，为高级别磋商取得实质性进展做好充分准备。'}

# result = es.create(index='news', doc_type='politics', id=3, body=data)

def bulk_insert():

    actions = []
    for i in range(1000 * 1000):
        action = {
            "_index": "tickets",
            "_type": "last",
            "_id": i+10,
            "_source": data
        }
        actions.append(action)
        i += 1

    helpers.bulk(es, actions)

    # start 19:22
    # stop


def search(keywords):
    body={
        "query" : {
                   "match_phrase" : {"content" : keywords}
                    }
         }


    rt1= es.search(index="scrapy-2019-09", body=body)
    #
    pp = pprint.PrettyPrinter(indent=1)
    pp.pprint(rt1)




if __name__ == '__main__':


    es = Elasticsearch(hosts="http://ngrok.eailab.cn:51011/")
    # # print(es.info())
    #
    # keywords = "东方证券"
    # search(keywords)

    bson_file = codecs.open('E:/Jockjo/data/news_roll/emym_normal.bson', 'rb')
    # emym_normal
    b = bson.decode_file_iter(bson_file)
    for index, item in enumerate(b):

        # print(item)
        # print(index, type(item))
        from bson.json_util import dumps
        del item['_id']
        # item["document"]
        # print(str(item["document"],'utf-8'))
        item["document"] = auto_decoding(item["document"], "utf8")
        item["title"] = item["title"].strip()
        item["news_time"] = item["news_time"].strip()
        item["document"] = item["document"]
        item = json.loads(dumps(item))
        item["news_time"] = dateConverter(item["news_time"])
        if "1900" in item["news_time"]:
            year = item["url"].split("/")[-1].split(",")[1][0:4]
            item["news_time"] = item["news_time"].replace("1900", year)
        print(item)
        # item = json.dumps(item, indent=4, sort_keys=True, ensure_ascii=False)











