# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 10:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faqcategory',
            options={
                'verbose_name': 'Kategorie',
                'verbose_name_plural': 'Kategorien'
            },
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Frage',
                     'verbose_name_plural': 'Fragen'},
        ),
    ]
