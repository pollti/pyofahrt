# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 18:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0027_auto_20161110_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='begin',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 11, 0, 0), verbose_name='Start'),
        ),
        migrations.AlterField(
            model_name='slot',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 11, 0, 0), verbose_name='Ende'),
        ),
    ]