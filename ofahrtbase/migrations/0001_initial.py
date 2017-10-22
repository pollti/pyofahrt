# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('key', models.CharField(
                    max_length=30, verbose_name='Eigenschaft')),
                ('value', models.BooleanField(verbose_name='Wert')),
            ],
        ),
    ]
