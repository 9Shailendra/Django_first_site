from django.contrib import admin
from .models import News
from django.db import models
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
from .models import News

# Register your models here.

# @admin.register(News)
# class NewsAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('title',)}
#     list_display = ('title', 'created_at')



class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')

try:
    admin.site.register(News, NewsAdmin)
except AlreadyRegistered:
    pass