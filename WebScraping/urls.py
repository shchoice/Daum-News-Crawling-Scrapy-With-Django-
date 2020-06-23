from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('scraping/', include('scraping.urls')),
    path('webuser/', include('webuser.urls')),
    path('newsscrapy/', include('newsscrapy.urls')),
]
