# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-01-02 20:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 2, 20, 56, 1, 853251, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 2, 20, 56, 1, 852250, tzinfo=utc)),
        ),
    ]