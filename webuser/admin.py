from django.contrib import admin
from .models import WebUser

# Register your models here.
class WebUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'password', 'register_date')

admin.site.register(WebUser, WebUserAdmin)