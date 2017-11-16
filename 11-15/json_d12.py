# -*- coding: utf-8 -*-
import urllib2
import json
import jsonpath
import codecs
url = 'http://tieba.baidu.com/present/getForumRank?user_id=471041060&forum_id=113893&pn=0&ps=4&type=1'
headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}

request = urllib2.Request(url, headers=headers)
res = urllib2.urlopen(request)
html = res.read()
unicodestr = json.loads(html)
gift_list = jsonpath.jsonpath(unicodestr, '$..gift_list')[0]
#print gift_list

array=json.dumps(gift_list, ensure_ascii=False)
#array=json.dumps(gift_list)
# with codecs.open('1.json', 'w','utf-8') as f:
#     f.write(str(gift_list))
f = codecs.open('1.json', 'w', 'utf-8')
f.write(array)
f.close()