# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Book', '0016_auto_20170704_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_details',
            name='det_id',
            field=models.CharField(default='null', max_length=20),
        ),
        migrations.AlterField(
            model_name='book_details',
            name='price',
            field=models.IntegerField(default=1, max_length=100),
        ),
    ]
