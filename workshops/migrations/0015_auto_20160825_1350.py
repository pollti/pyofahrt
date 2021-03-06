# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 11:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0014_auto_20160507_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='begin',
            field=models.DateTimeField(
                default=datetime.datetime(2016, 11, 11, 0, 0),
                verbose_name='Start'),
        ),
        migrations.AlterField(
            model_name='slot',
            name='end',
            field=models.DateTimeField(
                default=datetime.datetime(2016, 11, 11, 0, 0),
                verbose_name='Ende'),
        ),
        migrations.AlterField(
            model_name='slot',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Bezeichnung'),
        ),
    ]
