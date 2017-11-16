# -*- coding:utf-8 -*-

import urllib
import urllib2

# 通过抓包的方式获取的url，并不是浏览器上显示的url
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=null"

# 完整的headers
headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "OUTFOX_SEARCH_USER_ID_NCOO=1530166962.2672875; UM_distinctid=15e27c14e63acb-062b4cbd76a62d-6315107d-1fa400-15e27c14e647d4; P_INFO=mojigggg@gmail.com|1502950390|2|study|11&99|null&null&null#shh&null#10#0#0|&0||mojigggg@gmail.com; _ntes_nnid=cd561a6d698dfd214a40677cce980ed2,1509516065701; JSESSIONID=aaadJu5KFTWgsgIKf2K_v; SESSION_FROM_COOKIE=fanyiweb; OUTFOX_SEARCH_USER_ID=1491773951@106.2.43.11; ___rl__test__cookies=1510299170879",
    "Host": "fanyi.youdao.com",
    "Origin":"http//fanyi.youdao.com",
    "Pragma": "no-cache",
    "Referer":"http://fanyi.youdao.com/",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
}

# 用户接口输入
key = raw_input("请输入需要翻译的文字:")

# 发送到web服务器的表单数据
formdata = {
    "i": key,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "1510299170886",
    "sign": "530f76b414d61bfe267447c4fac1b485",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_CLICKBUTTION",
    "typoResult": "false",
}

# 经过urlencode转码
data = urllib.urlencode(formdata)

# 如果Request()方法里的data参数有值，那么这个请求就是POST
# 如果没有，就是Get
request = urllib2.Request(url, data=data, headers=headers)

print urllib2.urlopen(request).read()
