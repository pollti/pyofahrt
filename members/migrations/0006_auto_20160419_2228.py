# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 20:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20160419_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='base',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='ofahrtbase.Ofahrt'),
        ),
    ]
