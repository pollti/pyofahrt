# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 11:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_auto_20160423_2058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orgacandidate',
            options={
                'verbose_name': 'Orgabewerber',
                'verbose_name_plural': 'Orgabewerber'
            },
        ),
        migrations.AlterModelOptions(
            name='workshopcandidate',
            options={
                'verbose_name': 'Workshopbewerber',
                'verbose_name_plural': 'Workshopbewerber'
            },
        ),
    ]
