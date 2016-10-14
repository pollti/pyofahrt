# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Titel')),
                ('description', models.TextField(blank=True, verbose_name='Beschreibung')),
            ],
        ),
    ]
