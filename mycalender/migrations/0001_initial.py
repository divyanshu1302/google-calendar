# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-23 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('starts', models.CharField(max_length=10)),
                ('ends', models.CharField(max_length=10)),
                ('all_day', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
    ]
