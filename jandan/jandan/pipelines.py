# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.utils.project import get_project_settings  # 获得settings.py
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import scrapy
import os


class MyJandanPipeline(ImagesPipeline):
    # 获取settings文件里设置的变量值
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        image_url = item["image_link"]
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]  # 获取图片的hash值名字

        # if os.path.exists(self.IMAGES_STORE + "\\" + item['dir_name']):
        #     pass
        # else:
        #     os.makedirs(self.IMAGES_STORE + "\\" + item['dir_name'])

        if not image_path:
            raise DropItem('Item contains no images')
        else:
            os.rename(self.IMAGES_STORE + "\\" + image_path[0],
                      self.IMAGES_STORE + "\\" + item['nick_name'] + image_path[0][-10:-4] + ".jpg")
        item["image_path"] = self.IMAGES_STORE + "/" + item["nick_name"]

        return item
