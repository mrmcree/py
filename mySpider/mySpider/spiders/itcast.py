# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import MyspiderItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['http://www.itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#']

    def parse(self, response):
        teacher_list = response.xpath('//div[@class="li_txt"]')
        teacherItem = []
        for each in teacher_list:
            item = MyspiderItem()
            name = each.xpath('./h3/text()').extract()
            title = each.xpath('./h4/text()').extract()
            info = each.xpath('./p/text()').extract()

            item['name']=name[0].encode('gbk')
            item['title']=title[0].encode('gbk')
            item['info']=info[0].encode('gbk')

            yield item
            # teacherItem.append(item)
        # return teacherItem