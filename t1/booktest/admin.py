# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from models import *

class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 3

# 管理页面显示的信息
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_data']
    list_filter = ['btitle']
    search_fields = ['btitle']
    # list_per_page = 10 分页
    fieldsets = [
        ('base',{'fields':['btitle']}),
        ('super',{'fields':['bpub_data']}),
    ]
    inlines = [HeroInfoInline]
admin.site.register(BookInfo,BookInfoAdmin)

admin.site.register(HeroInfo)