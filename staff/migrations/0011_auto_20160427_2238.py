# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0010_workshopcandidate_workshop_ideas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshopcandidate',
            name='workshop_ideas',
        ),
        migrations.AddField(
            model_name='workshopcandidate',
            name='workshop_ideas',
            field=models.TextField(
                default='',
                help_text=
                'Bei mehreren Ideen, bitte eine Zeile pro Idee verwenden.',
                verbose_name='Workshopideen'),
            preserve_default=False,
        ),
    ]
