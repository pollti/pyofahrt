# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-17 21:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'permissions': (('can_use', 'Wikikomponente nutzen'),), 'verbose_name': 'Artikel', 'verbose_name_plural': 'Artikel'},
        ),
    ]