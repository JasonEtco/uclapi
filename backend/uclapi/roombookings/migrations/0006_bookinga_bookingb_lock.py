# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roombookings', '0005_auto_20170216_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingA',
            fields=[
                ('setid', models.CharField(blank=True, max_length=40, null=True)),
                ('siteid', models.CharField(blank=True, max_length=40, null=True)),
                ('roomid', models.CharField(blank=True, max_length=160, null=True)),
                ('sitename', models.CharField(blank=True, max_length=320, null=True)),
                ('roomname', models.CharField(blank=True, max_length=320, null=True)),
                ('bookabletype', models.CharField(blank=True, max_length=40, null=True)),
                ('slotid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('bookingid', models.CharField(blank=True, max_length=80, null=True)),
                ('starttime', models.CharField(blank=True, max_length=80, null=True)),
                ('finishtime', models.CharField(blank=True, max_length=20, null=True)),
                ('startdatetime', models.DateTimeField(blank=True, null=True)),
                ('finishdatetime', models.DateTimeField(blank=True, null=True)),
                ('weeknumber', models.FloatField(blank=True, null=True)),
                ('condisplayname', models.CharField(blank=True, max_length=4000, null=True)),
                ('phone', models.CharField(blank=True, max_length=160, null=True)),
                ('descrip', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookingB',
            fields=[
                ('setid', models.CharField(blank=True, max_length=40, null=True)),
                ('siteid', models.CharField(blank=True, max_length=40, null=True)),
                ('roomid', models.CharField(blank=True, max_length=160, null=True)),
                ('sitename', models.CharField(blank=True, max_length=320, null=True)),
                ('roomname', models.CharField(blank=True, max_length=320, null=True)),
                ('bookabletype', models.CharField(blank=True, max_length=40, null=True)),
                ('slotid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('bookingid', models.CharField(blank=True, max_length=80, null=True)),
                ('starttime', models.CharField(blank=True, max_length=80, null=True)),
                ('finishtime', models.CharField(blank=True, max_length=20, null=True)),
                ('startdatetime', models.DateTimeField(blank=True, null=True)),
                ('finishdatetime', models.DateTimeField(blank=True, null=True)),
                ('weeknumber', models.FloatField(blank=True, null=True)),
                ('condisplayname', models.CharField(blank=True, max_length=4000, null=True)),
                ('phone', models.CharField(blank=True, max_length=160, null=True)),
                ('descrip', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookingA', models.BooleanField()),
                ('bookingB', models.BooleanField()),
            ],
        ),
    ]
