# -*- coding: utf-8 -*-
import random
import base64
from settings import USER_AGENT
from settings import PROXYS
class RandomUserAgent(object):
    def process_request(self,request,spider):
        useragent=random.choice(USER_AGENT)
        # print useragent
        request.headers.setdefault("User-Agent", useragent)

class RandomProxy(object):
    def process_request(self,request,spider):
        proxy=random.choice(PROXYS)
        # print proxy
        pass
        # if proxy['user_paswd'] is None:
        #     # 没有代理账户验证的代理使用方式
        #     request.meta['proxy'] = "http://" + proxy['ip_port']
        #
        # else:
        #     # 对账户密码进行base64编码转换
        #     base64_userpasswd = base64.b64encode(proxy['user_paswd'])
        #     # 对应到代理服务器的信令格式里
        #     request.headers['Proxy-Authorization'] = 'Basic ' + base64_userpasswd
        #
        #     request.meta['proxy'] = "http://" + proxy['ip_port']