# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 11:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0007_auto_20160425_1344'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workshopcandidate',
            options={
                'permissions': (('group_full', 'Gruppe ist voll'), ),
                'verbose_name': 'Workshopbewerber',
                'verbose_name_plural': 'Workshopbewerber'
            },
        ),
    ]
