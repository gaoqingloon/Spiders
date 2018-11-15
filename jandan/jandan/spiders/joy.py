# -*- coding: utf-8 -*-
import scrapy
from jandan.items import JandanItem


class JoySpider(scrapy.Spider):
    name = 'joy'
    allowed_domains = ['jandan.net']

    offset = 1
    url = "http://jandan.net/ooxx/page-"
    start_urls = [url + str(offset)]

    def parse(self, response):
        # 每一页所有链接集合
        # links = response.xpath('//div[@class="text"]/p/a[@class="view_img_link"]/@href').extract()  # 得到一个列表
        links = response.xpath('//div[@class="text"]/p/img/@src').extract()  # 得到一个列表

        for link in links:
            # 做了反爬虫机制
            # print link
            item = JandanItem()
            item['image_link'] = "http:" + link
            item['nick_name'] = link.replace(':', '').replace('/', '').replace('.', '')[-10:-4]

            yield item

        # 停止条件，下一页
        self.offset += 1
        if self.offset <= 20:
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
