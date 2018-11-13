# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import KcomicItem


class KcomicInsawaSpider(CrawlSpider):
    name = 'insawa'
    allowed_domains = ['www.gumua.com']
    start_urls = ['http://www.gumua.com/Manhua/27999_1311.html']

    rules = (
        Rule(LinkExtractor(allow='/Manhua/27999_13\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # i = {}

        item = KcomicItem()

        item['img_urls'] = response.xpath("//div[@class='r_img ']/img/@src").extract()
        item['urls_lens'] = len(item['img_urls'])
        pageurl = response.xpath("/html/head/link[2]/@href").extract()
        item['chapter_name'] = 'chapter_' + ''.join(pageurl).split('_')[1][:-6]

        yield item

        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
