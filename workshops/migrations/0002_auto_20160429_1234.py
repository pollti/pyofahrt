# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 10:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workshops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('name', models.CharField(
                    max_length=30, verbose_name='Bezeichnung')),
                ('begin', models.DateTimeField(verbose_name='Start')),
                ('end', models.DateTimeField(verbose_name='Ende')),
            ],
            options={
                'verbose_name': 'Zeitslot',
                'verbose_name_plural': 'Zeitslots',
            },
        ),
        migrations.AlterModelOptions(
            name='workshop',
            options={
                'verbose_name': 'Workshop',
                'verbose_name_plural': 'Workshops'
            },
        ),
        migrations.AddField(
            model_name='workshop',
            name='host',
            field=models.ManyToManyField(
                to=settings.AUTH_USER_MODEL, verbose_name='Workshopanbieter'),
        ),
    ]
