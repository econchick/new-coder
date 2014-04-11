#! -*- coding: utf-8 -*-

"""
Web Scraper Project

Scrape data from a regularly updated website livingsocial.com and
save to a database (postgres).

Scrapy spider part - it actually performs scraping.
"""

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

from scraper_app.items import LivingSocialDeal


class LivingSocialSpider(Spider):
    """Spider for regularly updated livingsocial.com site, San Francisco page"""
    name = "livingsocial"
    allowed_domains = ["livingsocial.com"]
    start_urls = ["http://www.livingsocial.com/cities/15-san-francisco"]

    deals_list_xpath = '//li[@dealid]'
    item_fields = {'title': './/a/div[@class="deal-bottom"]/h3[@itemprop]/text()',
                   'link': './/a/@href',
                   'description': './/a/div[@class="deal-bottom"]/p/text()',
                   'category': './/a/div[@class="deal-top"]/div[@class="deal-category"]/span/text()',
                   'location': './/a/div[@class="deal-top"]/ul[@class="unstyled deal-info"]/li/text()',
                   'original_price': './/a/div[@class="deal-bottom"]/ul[@class="unstyled deal-info"]/li[@class="deal-original"]/del/text()',
                   'price': './/a/div[@class="deal-bottom"]/ul[@class="unstyled deal-info"]/li[@class="deal-price"]/text()'}

    def parse(self, response):
        """
        Default callback used by Scrapy to process downloaded responses

        Testing contracts:
        @url http://www.livingsocial.com/cities/15-san-francisco
        @returns items 1
        @scrapes title link

        """
        selector = Selector(response)

        # iterate over deals
        for deal in selector.xpath(self.deals_list_xpath):
            loader = ItemLoader(LivingSocialDeal(), selector=deal)

            # define processors
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            # iterate over fields and add xpaths to the loader
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()
