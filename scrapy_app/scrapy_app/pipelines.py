# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from pydispatch import dispatcher
from scrapy import signals

from newsscrapy.models import ScrapyItem


class ScrapyAppPipeline(object):
    def __init__(self, unique_id, *args, **kwargs):
        self.unique_id = unique_id
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            unique_id=crawler.settings.get('unique_id'),
        )

    def process_item(self, item, spider):
        scrapy_item = ScrapyItem()
        scrapy_item.news_topic = item['news_topic']
        scrapy_item.news_topic_detail = item['news_topic_detail']
        scrapy_item.news_headline = item['news_headline']
        scrapy_item.news_url = item['news_url']
        scrapy_item.news_company = item['news_company']
        scrapy_item.news_time = item['news_time']
        scrapy_item.news_contents = item['news_contents']
        scrapy_item.news_comments = item['news_comments']

        scrapy_item.save()
        return item

    def spider_closed(self, spider):
        print('SPIDER FINISHED!')
