from django.contrib import admin
from .models import ScrapyItem


class DaumNewsScrapingAdmin(admin.ModelAdmin):
    list_display = ('news_topic', 'news_topic_detail', 'news_headline', 'news_url',
     'news_company','news_time', 'news_contents', 'news_comments', 'register_date')

admin.site.register(ScrapyItem, DaumNewsScrapingAdmin)