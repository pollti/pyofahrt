# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 21:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ofahrtbase', '0009_auto_20160419_2316'),
        ('members', '0007_auto_20160419_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomAssignment',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('base', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='ofahrtbase.Ofahrt',
                    verbose_name='Zugehörige Ofahrt')),
                ('members', models.ManyToManyField(
                    to='members.Member', verbose_name='Zugewiesene Personen')),
                ('room', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='ofahrtbase.Room',
                    verbose_name='Zugehöriger Raum')),
            ],
            options={
                'verbose_name': 'Raumzuteilung',
                'verbose_name_plural': 'Raumzuteilungen',
            },
        ),
        migrations.AlterUniqueTogether(
            name='roomassignment',
            unique_together=set([('base', 'room')]),
        ),
    ]
