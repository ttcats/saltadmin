# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrepreneur',
            name='statu',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entrepreneur',
            name='working',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='com',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 31, 16, 29, 21, 930602)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='createtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 31, 16, 29, 21, 929683)),
            preserve_default=True,
        ),
    ]
