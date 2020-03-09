# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import ShiyanlouItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spider import Rule

class GithubSpider(scrapy.spiders.CrawlSpider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/shiyanlou?tab=repositories']
    
    rules = (Rule(
        LinkExtractor(
            allow='https://github.com/shiyanlou\?after=*'),
        callback='parse_item',
        follow=True),
        Rule(
            LinkExtractor(
                allow='https://github.com/shiyanlou\?tab=repositories$'),
            callback='parse_item',
            follow=True),)

    def parse_item(self, response):
        item = ShiyanlouItem()
        for data in response.css('li.col-12'):
            item['repo_name'] = data.xpath('.//h3/a/text()').extract_first().strip()
            item['update_time'] = data.xpath('.//relative-time/@datetime'
                    ).extract_first()
            yield item
