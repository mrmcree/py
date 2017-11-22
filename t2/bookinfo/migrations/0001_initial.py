# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 10:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.CharField(max_length=200)),
                ('bpub_data', models.DateTimeField(db_column='creat_time')),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=200)),
                ('hgender', models.BooleanField()),
                ('hcontent', models.CharField(max_length=1000)),
                ('hbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookinfo.BookInfo')),
            ],
        ),
    ]
