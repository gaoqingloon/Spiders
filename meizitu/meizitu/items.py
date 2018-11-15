# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeizituItem(scrapy.Item):
    nick_name = scrapy.Field()
    image_link = scrapy.Field()
    dir_name = scrapy.Field()
