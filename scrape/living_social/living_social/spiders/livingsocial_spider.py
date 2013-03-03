#! -*- coding: utf-8 -*-

"""
Web Scraper Project

Scrape data from a regularly updated website livingsocial.com and
save to a database (postgres).

Scrapy spider part - it actually performs scraping.
"""

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

from living_social.items import LivingSocialDeal


class LivingSocialSpider(BaseSpider):
    """Spider for regularly updated livingsocial.com site, New York page"""
    name = "livingsocial"
    allowed_domains = ["livingsocial.com"]
    start_urls = ["http://www.livingsocial.com/cities/1719-newyork-citywide"]

    deals_list_xpath = '//ul[@class="unstyled cities-items"]/li[@dealid]'
    item_fields = {'title': './/a/div[@class="bd"]/h1/text()',
                   'link': './/a/@href',
                   'description': './/a/div[@class="bd"]/h2/text()',
                   'category': './/@data-categories',
                   'location': './/a/div[@class="hd"]/div[@class="meta"]/span/text()',
                   'original_price': './/a/div[@class="bd"]/p[@class="meta"]/span[@class="original-price"]/del/text()',
                   'price': './/a/div[@class="bd"]/p[@class="meta"]/span[@class="price"]/text()'}

    def parse(self, response):
        """
        Default callback used by Scrapy to process downloaded responses

        Testing contracts:
        @url http://www.livingsocial.com/cities/1719-newyork-citywide
        @returns items 1
        @scrapes title link
        """
        selector = HtmlXPathSelector(response)

        # iterate over deals
        for deal in selector.select(self.deals_list_xpath):
            loader = XPathItemLoader(LivingSocialDeal(), selector=deal)

            # define processors
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            # iterate over fields and add xpaths to the loader
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()
