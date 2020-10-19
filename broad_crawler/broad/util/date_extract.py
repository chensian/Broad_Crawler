#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author:SingWeek
import re
from collections import Counter

from broad.util.encodeUtil import dateConverter


def extract_date(content):
    date_reg_exp = re.compile('\d{4}[-/]\d{2}[-/]\d{2}')
    matches_list=date_reg_exp.findall(content)
    standard_matches = []
    for match in matches_list:
        standard_time = dateConverter(match)
        if standard_time != "":
            standard_matches.append(standard_time)
    if len(standard_matches) > 0:
        date_str = Counter(standard_matches).most_common(1)[0][0]
        return date_str
    else:
        return None


if __name__ == '__main__':
    content = "如这样的日期2016-12-35也可以匹配到.2016-12-35测试如下."
    print(extract_date(content))
