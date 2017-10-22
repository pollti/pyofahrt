# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-08 21:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ofahrtbase', '0013_remove_ofahrt_year'),
        ('members', '0016_auto_20160503_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='room',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='ofahrtbase.Room',
                verbose_name='Zugeteilter Raum'),
        ),
        migrations.AlterUniqueTogether(
            name='roomassignment',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='roomassignment',
            name='base',
        ),
        migrations.RemoveField(
            model_name='roomassignment',
            name='members',
        ),
        migrations.RemoveField(
            model_name='roomassignment',
            name='room',
        ),
        migrations.DeleteModel(name='RoomAssignment', ),
    ]
