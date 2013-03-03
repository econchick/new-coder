#! -*- coding: utf-8 -*-

"""
Web Scraper Project

Scrape data from a regularly updated website livingsocial.com and
save to a database (postgres).

Scrapy item part - defines container for scraped data.
"""

from scrapy.item import Item, Field


class LivingSocialItem(Item):
    """Livingsocial container (dictionary-like object) for scraped data"""
    title = Field()
    description = Field()
    link = Field()
    category = Field()
    location = Field()
    original_price = Field()
    price = Field()
