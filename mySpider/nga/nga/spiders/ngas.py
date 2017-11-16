# -*- coding: utf-8 -*-
import scrapy

from nga.items import NgaItem


class NgaSpider(scrapy.Spider):
    name = 'nga'
    allowed_domains = ['nga.cn']
    url = 'http://bbs.ngacn.cc/thread.php?fid=431&page='
    offset = 0
    start_urls = [
        url + str(offset)
    ]

    def parse(self, response):
        for each in response.xpath('//tr[@class="row1 topicrow"] | //tr[@class="row2 topicrow"]'):
            item = NgaItem()
            item['postTitle'] = each.xpath("./td[@class='c2']/a[@class='topic']/text()").extract()[0]
            item['postTime'] = each.xpath("./td[@class='c3']/span/text()").extract()[0]
            item['postAuthor'] = each.xpath("./td[@class='c4']/span/text()").extract()[0]
            yield item

        if self.offset < 5:
            self.offset += 1
        yield scrapy.Request(self.url + str(self.offset), meta={'key': item}, callback=self.parse2)

