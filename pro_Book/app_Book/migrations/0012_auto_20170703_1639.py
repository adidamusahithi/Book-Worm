# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Book', '0011_auto_20170703_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_details',
            name='reviews',
        ),
        migrations.AddField(
            model_name='book_details',
            name='rate',
            field=models.IntegerField(default=1),
        ),
    ]
