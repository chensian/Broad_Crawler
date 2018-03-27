#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/27 23:16 
# @Author  : chesian
# @Site    : 
# @File    : db.py
# @Software: PyCharm
import json

import redis


class RedisDBUtil():
    conn = None

    def get_connect(self):
        if not self.conn:
            self.conn = redis.Redis(host='localhost', port=6379, db=0)
        return self.conn

    def set_value(self, name, value):
        self.get_connect().set(name=name, value=value)

    def get_value(self, name):
        value = self.get_connect().get(name=name)
        if value:
            value = json.loads(value)
        return value

    def del_value(self, name):
        self.get_connect().delete(name)

if __name__ == "__main__":
    pass

