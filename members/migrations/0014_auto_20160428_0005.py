# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 22:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0002_logentry_remove_auto_add'),
        ('members', '0013_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='user_ptr',
        ),
        migrations.DeleteModel(name='Person', ),
    ]
