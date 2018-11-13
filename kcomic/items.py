# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KcomicItem(scrapy.Item):
    img_urls = scrapy.Field()
    urls_lens = scrapy.Field()
    chapter_name = scrapy.Field()

    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
