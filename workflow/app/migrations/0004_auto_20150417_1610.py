# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150401_1626'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branches',
            options={'verbose_name': '\u90e8\u95e8', 'verbose_name_plural': '\u90e8\u95e8'},
        ),
        migrations.AlterModelOptions(
            name='com',
            options={'verbose_name': '\u8bc4\u8bba', 'verbose_name_plural': '\u8bc4\u8bba'},
        ),
        migrations.AlterModelOptions(
            name='entrepreneur',
            options={'verbose_name': '\u7ef4\u62a4\u4eba\u5458', 'verbose_name_plural': '\u7ef4\u62a4\u4eba\u5458'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': '\u5de5\u5355', 'verbose_name_plural': '\u5de5\u5355'},
        ),
        migrations.AlterModelOptions(
            name='floors',
            options={'verbose_name': '\u697c\u5c42', 'verbose_name_plural': '\u697c\u5c42'},
        ),
        migrations.AlterModelOptions(
            name='grades',
            options={'verbose_name': '\u6545\u969c\u7b49\u7ea7', 'verbose_name_plural': '\u6545\u969c\u7b49\u7ea7'},
        ),
        migrations.AlterModelOptions(
            name='problems',
            options={'verbose_name': '\u6545\u969c\u7c7b\u578b', 'verbose_name_plural': '\u6545\u969c\u7c7b\u578b'},
        ),
        migrations.AlterModelOptions(
            name='score',
            options={'verbose_name': '\u8bc4\u5206\u7b49\u7ea7', 'verbose_name_plural': '\u8bc4\u5206\u7b49\u7ea7'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': '\u72b6\u6001', 'verbose_name_plural': '\u72b6\u6001'},
        ),
        migrations.RenameField(
            model_name='entrepreneur',
            old_name='statu',
            new_name='e_mail',
        ),
        migrations.AddField(
            model_name='entrepreneur',
            name='ipone',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='com',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 17, 16, 10, 1, 527409)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='createtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 17, 16, 10, 1, 526394)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='floor',
            field=models.ForeignKey(default=b'1', to='app.Floors'),
            preserve_default=True,
        ),
    ]
