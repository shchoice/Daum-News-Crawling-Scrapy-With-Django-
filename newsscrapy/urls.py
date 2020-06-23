from django.contrib import admin
from django.conf import settings
from django.conf.urls import static
from django.urls import re_path, path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('collect/', views.NewsDataCollect.as_view())
]