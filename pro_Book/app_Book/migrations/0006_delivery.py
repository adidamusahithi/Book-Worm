# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Book', '0005_book_details_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('phNo', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=20)),
            ],
        ),
    ]
