# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 20:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0016_auto_20161110_0311'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StaffRoomAssignement',
            new_name='StaffRoomAssignment',
        ),
    ]