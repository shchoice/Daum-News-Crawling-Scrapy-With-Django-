from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import ImageScrapingForm, NewsScrapingForm
from .models import ImageScraping, NewsScraping
from scraping.img_download import ImageScraper
from scraping.newsscraping import NewsScraper

# Create your views here.
def home(request):
    return render(request, "scraping/main.html")


class ImageDataCollect(FormView):
    template_name = "scraping/imgscraping.html"
    form_class = ImageScrapingForm
    success_url = "/scraping/imgscraping/"

    def form_valid(self, form):
        scraping = ImageScraping(
            image_keyword = form.data.get('image_keyword'),
            image_site = form.data.get('image_site'),
            image_purpose = form.data.get('image_purpose'),
            image_cycle = form.data.get('image_cycle'),
            image_save_path = form.data.get('image_save_path'),
        )
        scraping.save()

        image_keyword = form.data.get('image_keyword')
        image_save_path = form.data.get('image_save_path')


        keywords = image_keyword.split(' ')
        with open("keywords.txt", 'w+', encoding="utf-8") as f:
            for keyword in keywords:
                print(keyword)
                f.write(f'{keyword}\n')          

        image_scraper = ImageScraper(4, True, True, image_save_path)
        image_scraper.scraping_start()

        return super().form_valid(form)

class NewsDataCollect(FormView):
    template_name = "scraping/newsscraping.html"
    form_class = NewsScrapingForm
    success_url = "/scraping/newsscraping"


    def form_valid(self, form):
        scraping = NewsScraping(
            news_keyword = form.data.get('news_keyword'),
            news_site = form.data.get('news_site'),
            news_purpose = form.data.get('news_purpose'),
            news_cycle = form.data.get('news_cycle'),
            news_search_num = form.data.get('news_search_num'),
            news_save_path = form.data.get('news_save_path'),
        )
        scraping.save()     

        news_scraping = NewsScraper("인공지능", 100)
        news_scraping.scraping_start()

        return super().form_valid(form)

        