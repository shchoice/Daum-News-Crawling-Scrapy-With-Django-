from django import forms
from .models import ScrapyItem

class ScrapyItemForm(forms.Form):
    news_purpose = forms.CharField(error_messages={'required' : '수집 용도를 입력해주세요.'}, max_length=64, label='수집 용도')

    def clean(self):
        cleaned_data = super().clean()
        news_purpose = cleaned_data.get('news_purpose')

        if not news_purpose:
            self.add_error('news_purpose', "수집 목적을 입력하지 않았습니다.")