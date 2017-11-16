# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import time
class NgaPipeline(object):
    def __init__(self):
        self.filename=open('nga.json','w')
    def process_item(self, item, spider):
        item['postTime']= str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(item['postTime']))))
        text = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.filename.write(text.encode('gbk'))
        return item
    def close_spider(self,spider):
        self.filename.close()