# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 00:46
from __future__ import unicode_literals

import dashboard.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0003_auto_20170619_2242'),
        ('dashboard', '0007_app_callback_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='scope',
            field=models.ForeignKey(default=dashboard.models.App.create_scope, on_delete=django.db.models.deletion.CASCADE, to='oauth.OAuthScope'),
        ),
    ]
