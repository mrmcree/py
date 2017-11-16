# coding=utf-8
import urllib2

proxyswitch = True

httpproxy_handler = urllib2.ProxyHandler({'http': "61.158.111.142:53281"})

null_handler = urllib2.ProxyHandler({})

if proxyswitch:
    opener = urllib2.build_opener(httpproxy_handler)

else:
    opener = urllib2.build_opener(null_handler)

# 全局的open（）
urllib2.install_opener(opener)

req = urllib2.Request('http://www.baidu.com')
res = urllib2.urlopen(req)
print res.read()
 