# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=25)),
                ('actors', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='watchedlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('actor', models.CharField(max_length=50)),
                ('watched_date', models.DateTimeField(verbose_name='Watched date')),
            ],
        ),
    ]
