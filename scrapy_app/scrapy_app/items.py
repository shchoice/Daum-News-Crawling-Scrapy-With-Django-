# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from pydispatch import dispatcher
from scrapy import signals


class DaumNewsItem(scrapy.Item):
    news_topic = scrapy.Field()
    news_topic_detail = scrapy.Field()
    news_headline = scrapy.Field()
    news_url = scrapy.Field()
    news_company = scrapy.Field()
    news_time = scrapy.Field()
    news_contents = scrapy.Field()
    news_comments = scrapy.Field()