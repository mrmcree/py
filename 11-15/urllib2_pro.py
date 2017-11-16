# coding=utf-8
import urllib2

#http_handler = urllib2.HTTPHandler()
http_handler = urllib2.HTTPHandler(debuglevel=1)
opener = urllib2.build_opener(http_handler)

request = urllib2.Request('http://www.baidu.com')

response = opener.open(request)

#print response.read()
