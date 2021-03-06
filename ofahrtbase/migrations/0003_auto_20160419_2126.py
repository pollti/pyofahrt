# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 19:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ofahrtbase', '0002_ofahrt'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='base',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to='ofahrtbase.Ofahrt'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ofahrt',
            name='year',
            field=models.IntegerField(default=2016, verbose_name='Jahr'),
        ),
    ]
