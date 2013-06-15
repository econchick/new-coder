# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'livingsocial'

SPIDER_MODULES = ['living_social.spiders']

ITEM_PIPELINES = ['living_social.pipelines.LivingSocialPipeline']

DATABASE = {'drivername': 'postgres',
            'host': 'localhost',
            'port': '5432',
            'username': 'lynnroot',
            'password': '',
            'database': 'scrape'}
