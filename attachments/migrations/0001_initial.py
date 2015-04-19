# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.TextField(blank=True)),
                ('title', models.CharField(max_length=128)),
                ('file', models.FileField(upload_to=b'attachments/audio/%Y/%m/%d')),
                ('credit', models.ManyToManyField(related_name='news_audio', to='authors.Author', blank=True)),
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
                ('credit', models.ManyToManyField(related_name='news_image', to='authors.Author', blank=True)),
                ('request_type', models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True)),
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
                ('text', models.CharField(max_length=128)),
                ('votes', models.PositiveIntegerField(default=0)),
                ('question', models.ForeignKey(to='attachments.Poll')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.CharField(max_length=64)),
                ('line_1', models.CharField(max_length=128, blank=True)),
                ('line_2', models.CharField(max_length=128, blank=True)),
                ('rating', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10)])),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.TextField(blank=True)),
                ('title', models.CharField(max_length=128)),
                ('youtube_id', models.CharField(max_length=16)),
                ('credit', models.ManyToManyField(related_name='news_video', to='authors.Author', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
