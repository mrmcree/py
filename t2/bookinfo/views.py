# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import response, request, HttpResponse
from django.template import RequestContext, loader
from .models import *
# Create your views here.
def index(request):
    booklist = BookInfo.objects.all()
    return render(request, 'booktest/index.html', {'booklist': booklist})

def detail(request,id):
    book=BookInfo.objects.get(pk=id)
    herolist=book.heroinfo_set.all()
    return render(request,'booktest/detail.html',{'herolist':herolist})