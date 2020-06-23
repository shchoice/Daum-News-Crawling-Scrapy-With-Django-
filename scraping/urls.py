from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('imgscraping/', views.ImageDataCollect.as_view()),
    path('newsscraping/', views.NewsDataCollect.as_view()),
]
