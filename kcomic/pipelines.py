# -*- coding: utf-8 -*-

from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
import re

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class KcomicPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        imgcount = 0
        for img_url in item['img_urls']:
            imgcount += 1
            #ues meta to transport name and index to file_path
            yield Request(img_url, meta={'name':item['chapter_name'], 'index':str(imgcount)})

    def file_path(self, request, response=None, info=None):
        name = request.meta['name']
        index = request.meta['index'] + '.jpg'
        # name = re.sub(r'[？\\*|“<>:/]', '', name)
        filename = u'{0}/{1}'.format(name, index)
        return filename


    # def process_item(self, item, spider):
    #     return item


