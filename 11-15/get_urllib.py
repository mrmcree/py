# -*- coding:utf-8 -*-
import urllib
import urllib2

url = 'http://www.baidu.com/s'
headers = {
    'User-Agent': 'Mozilla'
}
keyword = raw_input('请输入关键字:')
wd = {'wd': keyword}
wd = urllib.urlencode(wd)
fullurl = url + '?' + wd
print  fullurl
request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)
