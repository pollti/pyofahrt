# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-09 14:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Gebäude',
                'verbose_name_plural': 'Gebäude',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Gelände',
                'verbose_name_plural': 'Gelände',
            },
        ),
        migrations.CreateModel(
            name='Ofahrt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_date', models.DateField(verbose_name='Anreisedatum')),
                ('end_date', models.DateField(verbose_name='Abreisedatum')),
                ('active', models.BooleanField(default=True, unique=True, verbose_name='Aktiv?')),
            ],
            options={
                'verbose_name': 'Ofahrtobjekt',
                'verbose_name_plural': 'Ofahrtobjekte',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('number', models.CharField(max_length=30)),
                ('capacity', models.IntegerField(default=0, help_text='Wie viele Teilnehmer passen in diesen Raum?', verbose_name='Kapazität')),
                ('usecase_sleep', models.BooleanField(default=False, verbose_name='Schlafraum')),
                ('usecase_workshop', models.BooleanField(default=False, verbose_name='Workshops')),
                ('usecase_outside', models.BooleanField(default=False, verbose_name='Freifläche')),
                ('usecase_store', models.BooleanField(default=False, verbose_name='Lagerraum')),
                ('usecase_meal', models.BooleanField(default=False, verbose_name='Essensraum')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ofahrtbase.Building')),
            ],
            options={
                'verbose_name': 'Raum',
                'verbose_name_plural': 'Räume',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50, unique=True, verbose_name='Schlüssel')),
                ('readable', models.CharField(max_length=50, unique=True, verbose_name='Eigenschaft')),
                ('value', models.BooleanField(verbose_name='Aktiv?')),
            ],
            options={
                'verbose_name': 'Einstellung',
                'verbose_name_plural': 'Einstellungen',
            },
        ),
        migrations.AddField(
            model_name='building',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ofahrtbase.Location'),
        ),
    ]
