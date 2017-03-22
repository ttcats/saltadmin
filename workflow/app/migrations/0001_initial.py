# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('branch', models.CharField(max_length=100, verbose_name=b'\xe9\x83\xa8\xe9\x97\xa8')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Com',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('envnt_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('time', models.DateTimeField(default=datetime.datetime(2015, 3, 29, 10, 56, 14, 583666))),
                ('content', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entrepreneur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entrepreneur', models.CharField(max_length=100, verbose_name=b'\xe7\xbb\xb4\xe6\x8a\xa4\xe4\xba\xba\xe5\x91\x98')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=100, null=True, blank=True)),
                ('createuser', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
                ('content', models.TextField()),
                ('img', models.ImageField(null=True, upload_to=b'photos', blank=True)),
                ('createtime', models.DateTimeField(default=datetime.datetime(2015, 3, 29, 10, 56, 14, 582761))),
                ('finishtime', models.DateTimeField(null=True, blank=True)),
                ('e_score', models.CharField(max_length=20, null=True, blank=True)),
                ('branch', models.ForeignKey(to='app.Branches')),
                ('enumerate', models.ForeignKey(default=b'1', to='app.Entrepreneur')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Floors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('floor', models.CharField(max_length=100, verbose_name=b'\xe6\xa5\xbc\xe5\xb1\x82')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.CharField(max_length=100, verbose_name=b'\xe6\x95\x85\xe9\x9a\x9c\xe7\xad\x89\xe7\xba\xa7')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ploblem', models.CharField(max_length=100, verbose_name=b'\xe6\x95\x85\xe9\x9a\x9c\xe7\xb1\xbb\xe5\x9e\x8b')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.CharField(max_length=100, verbose_name=b'\xe8\xaf\x84\xe5\x88\x86\xe7\xad\x89\xe7\xba\xa7')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=100, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='floor',
            field=models.ForeignKey(to='app.Floors'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='grade',
            field=models.ForeignKey(to='app.Grades'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='problem',
            field=models.ForeignKey(to='app.Problems'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.ForeignKey(default=b'1', to='app.Status'),
            preserve_default=True,
        ),
    ]
