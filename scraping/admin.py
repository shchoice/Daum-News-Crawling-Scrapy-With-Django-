from django.contrib import admin
from .models import ImageScraping, NewsScraping

# Register your models here.
class ImageScrapingAdmin(admin.ModelAdmin):
    list_display = ('image_site', 'image_keyword', 'image_purpose', 'image_cycle', 'image_save_path', 'register_date')

admin.site.register(ImageScraping, ImageScrapingAdmin)


class NewsScrapingAdmin(admin.ModelAdmin):
    list_display = ('news_site', 'news_keyword', 'news_search_num', 'news_purpose', 'news_cycle', 'news_save_path', 'register_date')

admin.site.register(NewsScraping, NewsScrapingAdmin)