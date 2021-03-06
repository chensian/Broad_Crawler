# encoding=utf-8
# ------------------------------------------
#   版本：3.0
#   日期：2016-12-01
#   作者：九茶<http://blog.csdn.net/bone_ace>
# ------------------------------------------


import random
import logging

from scrapy.spidermiddlewares.httperror import HttpErrorMiddleware

from broad.models.user_agent import Agents

logger = logging.getLogger(__name__)


class UserAgentMiddleware(object):
    """ 换User-Agent """

    def process_request(self, request, spider):
        agent = random.choice(Agents)
        request.headers["User-Agent"] = agent


#RedirectMiddleware.py

class RedirectMiddleware(HttpErrorMiddleware):

    def process_request(self, request, spider):
        if request.meta.has_key('enable_redirect'):
            pass


