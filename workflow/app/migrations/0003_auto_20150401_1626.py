# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150331_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrepreneur',
            name='time',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='com',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 1, 16, 26, 23, 675197)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='createtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 1, 16, 26, 23, 674276)),
            preserve_default=True,
        ),
    ]
