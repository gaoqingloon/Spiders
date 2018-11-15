# -*- coding: utf-8 -*-
import scrapy
from meizitu.items import MeizituItem


class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    allowed_domains = ['www.meizitu.com']

    offset = 1
    url = "http://www.meizitu.com/a/more_%s.html" % str(offset)
    start_urls = [url]

    def parse(self, response):
        # 每一页所有链接集合
        links = response.xpath('//div[@class="pic"]/a/@href').extract()  # 得到一个列表
        for link in links:
            yield scrapy.Request(link, callback=self.parse_item)

        # 停止条件，下一页
        self.offset += 1
        if self.offset <= 20:
            self.url = "http://www.meizitu.com/a/more_%s.html" % str(self.offset)
            yield scrapy.Request(self.url, callback=self.parse)

    def parse_item(self, response):
        item = MeizituItem()
        image_links = response.xpath('//div[@id="picture"]/p/img/@src').extract()
        item['dir_name'] = response.xpath('//div[@class="metaRight"]/h2/a/text()').extract()[0]

        for link in image_links:
            item['image_link'] = link
            item['nick_name'] = link.replace(':', '').replace('/', '')[39:-4]

            yield item
