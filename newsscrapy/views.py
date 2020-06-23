from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import ScrapyItemForm
from .models import ScrapyPurposeItem
import subprocess
import os

class NewsDataCollect(FormView):
    template_name = "newsscrapy/daum.html"
    form_class = ScrapyItemForm
    success_url = "/newsscrapy/collect"

    def form_valid(self, form):
        scraping = ScrapyPurposeItem(
            news_purpose = form.data.get('news_purpose'),
        )
        scraping.save()
        
        os.system("cd scrapy_app && scrapy crawl news -o news.json")

        return super().form_valid(form)

        