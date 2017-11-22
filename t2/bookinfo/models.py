# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class BookInfo(models.Model):

    btitle = models.CharField(max_length=200)
    bpub_data = models.DateTimeField(db_column='creat_time')
    def __str__(self):
        return self.btitle.encode('utf-8')

class HeroInfo(models.Model):

    hname = models.CharField(max_length=200)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    hbook = models.ForeignKey(BookInfo)
    def __str__(self):
        return self.hname.encode('utf-8')
