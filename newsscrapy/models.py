from django.db import models
from django.utils import timezone


class ScrapyItem(models.Model):
    news_topic = models.CharField(max_length=64, verbose_name="뉴스 주제")
    news_topic_detail = models.CharField(max_length=64, verbose_name="뉴스 소주제")
    news_headline = models.CharField(max_length=256, verbose_name="뉴스 제목")
    news_url = models.CharField(max_length=256, verbose_name="뉴스 URL")
    news_company = models.CharField(max_length=64, verbose_name="뉴스 회사")
    news_time = models.CharField(max_length=64, verbose_name="뉴스 시간")
    news_contents = models.TextField(verbose_name="뉴스 본문")
    news_comments = models.CharField(max_length=64, verbose_name="뉴스 댓글수")
    register_date = models.DateTimeField(auto_now_add=True, verbose_name="등록날짜")


    def __str__(self):
        return self.news_topic

    class Meta:
        db_table = "daum_news_scraping"
        verbose_name = "다음 뉴스"
        verbose_name_plural = "다음 뉴스"


class ScrapyPurposeItem(models.Model):
    news_purpose = models.CharField(max_length=64, verbose_name="수집 목적")

    def __str__(self):
        return self.news_topic

    class Meta:
        db_table = "daum_news_purpose"
        verbose_name = "다음 뉴스 목적(temp)"
        verbose_name_plural = "다음 뉴스 목적(temp)"
