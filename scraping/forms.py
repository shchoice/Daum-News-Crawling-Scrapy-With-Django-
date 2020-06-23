from django import forms
from .models import ImageScraping, NewsScraping

class ImageScrapingForm(forms.Form):
    image_keyword = forms.CharField(error_messages={'required' : '검색 내용을 입력해주세요.'}, max_length=64, label='검색 내용')
    image_site = forms.CharField(error_messages={'required' : '검색 사이트를 입력해주세요.'}, max_length=64, label='검색 사이트')
    image_purpose = forms.CharField(error_messages={'required' : '수집 용도를 입력해주세요.'}, max_length=64, label='수집 용도')
    image_cycle = forms.CharField(error_messages={'required' : '수집 주기를 입력해주세요.'}, max_length=64, label='수집 주기')
    image_save_path = forms.CharField(error_messages={'required' : '저장경로를 입력해주세요.'}, max_length=64, label='저장 경로')

    def clean(self):
        cleaned_data = super().clean()
        image_keyword = cleaned_data.get('image_keyword')
        image_site = cleaned_data.get('image_site')
        image_purpose = cleaned_data.get('image_purpose')
        image_cycle = cleaned_data.get('image_cycle')
        image_save_path = cleaned_data.get('image_save_path')

        if not (image_site and image_keyword and image_purpose and image_cycle, image_save_path):
            self.add_error('image_site', "검색 사이트를 입력하지 않았습니다.")
            self.add_error('image_keyword', "검색 내용을 입력하지 않았습니다.")
            self.add_error('image_purpose', "수집 목적을 입력하지 않았습니다.")
            self.add_error('image_cycle', "수집 주기를 입력하지 않았습니다.")
            self.add_error('image_save_path', "저장 경로를 입력하지 않았습니다.")



class NewsScrapingForm(forms.Form):
    news_keyword = forms.CharField(error_messages={'required' : '검색 내용을 입력해주세요.'}, max_length=64, label='검색 내용')
    news_site = forms.CharField(error_messages={'required' : '검색 사이트를 입력해주세요.'}, max_length=64, label='검색 사이트')
    news_purpose = forms.CharField(error_messages={'required' : '수집 용도를 입력해주세요.'}, max_length=64, label='수집 용도')
    news_cycle = forms.CharField(error_messages={'required' : '수집 주기를 입력해주세요.'}, max_length=64, label='수집 주기')
    news_search_num = forms.CharField(error_messages={'required' : '수집 개수를 입력해주세요.'}, max_length=64, label='수집 개수')
    news_save_path = forms.CharField(error_messages={'required' : '저장경로를 입력해주세요.'}, max_length=64, label='저장 경로')

    def clean(self):
        cleaned_data = super().clean()
        news_keyword = cleaned_data.get('news_keyword')
        news_site = cleaned_data.get('news_site')
        news_purpose = cleaned_data.get('news_purpose')
        news_cycle = cleaned_data.get('news_cycle')
        news_search_num = cleaned_data.get('news_search_num')
        news_save_path = cleaned_data.get('news_save_path')

        if not (news_site and news_keyword and news_purpose and news_cycle and news_search_num and news_save_path):
            self.add_error('news_site', "검색 사이트를 입력하지 않았습니다.")
            self.add_error('news_keyword', "검색 내용을 입력하지 않았습니다.")
            self.add_error('news_purpose', "수집 목적을 입력하지 않았습니다.")
            self.add_error('news_cycle', "수집 주기를 입력하지 않았습니다.")
            self.add_error('news_search_num', "수집 개수를 입력하지 않았습니다.")
            self.add_error('news_save_path', "저장 경로를 입력하지 않았습니다.")