# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Book', '0008_auto_20170703_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_details',
            name='ratings',
        ),
        migrations.AddField(
            model_name='book_details',
            name='reviews',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='book_list',
            name='Bname',
            field=models.CharField(max_length=10),
        ),
    ]
