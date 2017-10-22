# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-10 02:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ofahrtbase', '0019_auto_20161020_1750'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0015_auto_20161109_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffRoomAssignement',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('room', models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    to='ofahrtbase.Room',
                    verbose_name='Zugeteilter Raum')),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='stafftagbox',
            options={
                'verbose_name': 'Tagbox',
                'verbose_name_plural': 'Tagboxen'
            },
        ),
    ]
