# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-02 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0028_auto_20161110_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='begin',
            field=models.DateTimeField(default=None, verbose_name='Start'),
        ),
        migrations.AlterField(
            model_name='slot',
            name='end',
            field=models.DateTimeField(default=None, verbose_name='Ende'),
        ),
    ]
