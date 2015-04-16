# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.TextField(blank=True)),
                ('title', models.CharField(max_length=128)),
                ('file', models.FileField(upload_to=b'attachments/audio/%Y/%m/%d')),
            ],
            options={
                'verbose_name_plural': 'Audio',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.TextField(blank=True)),
                ('file', models.ImageField(upload_to=b'attachments/image/%Y/%m/%d')),
                ('request_id', models.PositiveIntegerField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=128)),
                ('is_open', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PollChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=128)),
                ('votes', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.CharField(max_length=64)),
                ('line_1', models.CharField(max_length=128, blank=True)),
                ('line_2', models.CharField(max_length=128, blank=True)),
                ('rating', models.PositiveIntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.TextField(blank=True)),
                ('title', models.CharField(max_length=128)),
                ('youtube_id', models.CharField(max_length=16)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
