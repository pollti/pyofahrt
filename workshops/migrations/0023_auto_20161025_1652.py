# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 14:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ofahrtbase', '0019_auto_20161020_1750'),
        ('workshops', '0022_slot_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slot',
            name='room',
        ),
        migrations.AddField(
            model_name='workshop',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ofahrtbase.Room', verbose_name='Zugeteilter Raum'),
        ),
    ]
