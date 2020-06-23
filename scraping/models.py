from django.db import models

class ImageScraping(models.Model):
    image_site = models.CharField(max_length=64, verbose_name="검색 사이트")
    image_keyword = models.CharField(max_length=64, verbose_name="검색 내용")
    image_purpose = models.CharField(max_length=64, verbose_name="수집 용도")
    image_cycle = models.CharField(max_length=64, verbose_name="수집 주기")
    image_save_path = models.CharField(max_length=64, verbose_name="저장 경로")
    register_date = models.DateTimeField(auto_now_add=True, verbose_name="등록날짜")


    def __str__(self):
        return self.image_keyword

    class Meta:
        db_table = "image_scraping"
        verbose_name = "이미지 수집 데이터"
        verbose_name_plural = "이미지 수집 데이터"


class NewsScraping(models.Model):
    news_site = models.CharField(max_length=64, verbose_name="검색 사이트")
    news_keyword = models.CharField(max_length=64, verbose_name="검색 내용")
    news_search_num = models.CharField(max_length=64, verbose_name="검색 개수")
    news_purpose = models.CharField(max_length=64, verbose_name="수집 용도")
    news_cycle = models.CharField(max_length=64, verbose_name="수집 주기")
    news_save_path = models.CharField(max_length=64, verbose_name="저장 경로")
    register_date = models.DateTimeField(auto_now_add=True, verbose_name="등록날짜")


    def __str__(self):
        return self.news_keyword 

    class Meta:
        db_table = "news_scraping"
        verbose_name = "뉴스 수집 데이터"
        verbose_name_plural = "뉴스 수집 데이터"