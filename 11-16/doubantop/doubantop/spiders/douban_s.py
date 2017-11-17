# -*- coding: utf-8 -*-
import scrapy
from doubantop.items import DoubantopItem


class DoubanSSpider(scrapy.Spider):
    name = 'douban_s'
    allowed_domains = ['movie.douban.com']
    offset=0

    url = 'http://movie.douban.com/top250?start='
    start_urls=[url+str(offset),]

    def parse(self, response):
        item = DoubantopItem()
        movies = response.xpath("//div[@class='info']")
        for each in movies:
            item['title'] = each.xpath('.//span[@class="title"][1]/text()').extract()[0]
            item['bd'] = each.xpath('.//div[@class="bd"]/p/text()').extract()[0].strip()
            item['star'] = each.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()

            item['quote'] = each.xpath(".//div[@class='bd']/p[@class='quote']/span[@class='inq']/text()").extract()
            yield item
        if self.offset<225:
            self.offset+=25
            yield scrapy.Request(self.url+str(self.offset),callback=self.parse)

