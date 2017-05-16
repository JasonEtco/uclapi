# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-16 20:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import oauth.app_helpers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0006_auto_20170516_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='OAuthScope',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('private_roombookings', models.BooleanField(default=False)),
                ('private_timetable', models.BooleanField(default=False)),
                ('private_uclu', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OAuthToken',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('token', models.CharField(default=oauth.app_helpers.generate_user_token, max_length=70, unique=True)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.App')),
                ('scope', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='oauth.OAuthScope')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.User')),
            ],
        ),
    ]