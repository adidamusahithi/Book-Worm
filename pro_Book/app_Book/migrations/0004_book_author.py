# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 08:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_Book', '0003_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_Book.Author')),
                ('Bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_Book.Book_List')),
            ],
        ),
    ]