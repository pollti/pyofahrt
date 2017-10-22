# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-08 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ofahrtbase', '0013_remove_ofahrt_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='capacity',
            field=models.IntegerField(
                default=0,
                help_text='Wie viele Teilnehmer passen in diesen Raum?',
                verbose_name='Kapazität'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='key',
            field=models.CharField(
                max_length=50, unique=True, verbose_name='Schlüssel'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='readable',
            field=models.CharField(
                max_length=50, unique=True, verbose_name='Eigenschaft'),
        ),
    ]
