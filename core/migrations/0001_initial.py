# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0001_initial'),
        ('authors', '0001_initial'),
        ('attachments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, blank=True)),
                ('slug', models.SlugField(max_length=128)),
                ('body', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('position', models.PositiveSmallIntegerField(unique=True)),
            ],
            options={
                'ordering': ['position'],
                'verbose_name_plural': 'Statuses',
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('assignment_slug', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=128, blank=True)),
                ('url_slug', models.SlugField(max_length=128, blank=True)),
                ('teaser', models.CharField(max_length=128, blank=True)),
                ('subhead', models.CharField(max_length=128, blank=True)),
                ('body', models.TextField(blank=True)),
                ('summary', models.TextField(blank=True)),
                ('angle', models.TextField(blank=True)),
                ('sources', models.TextField(blank=True)),
                ('late_run', models.BooleanField(default=False)),
                ('position', models.PositiveIntegerField(unique=True, db_index=True)),
                ('card_focus', models.CharField(default=b'cc', max_length=2, choices=[(b'cc', b'center center'), (b'cl', b'center left'), (b'cr', b'center right'), (b'tl', b'top left'), (b'tc', b'top center'), (b'tr', b'top right'), (b'bl', b'bottom left'), (b'bc', b'bottom center'), (b'br', b'bottom right')])),
                ('feature_card_image', models.BooleanField(default=True)),
                ('publish_time', models.DateTimeField()),
                ('breaking_duration', models.PositiveSmallIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('alternate_template', models.ForeignKey(blank=True, to='display.Template', null=True)),
                ('authors', models.ManyToManyField(related_name='news_story', to='authors.Author', blank=True)),
                ('card', models.ForeignKey(related_name='news_article_card', blank=True, to='attachments.Image', null=True)),
                ('card_size', models.ForeignKey(to='display.CardSize')),
                ('featured_audio', models.ForeignKey(blank=True, to='attachments.Audio', null=True)),
                ('featured_image', models.ForeignKey(related_name='news_article_featured_image', blank=True, to='attachments.Image', null=True)),
                ('featured_video', models.ForeignKey(blank=True, to='attachments.Video', null=True)),
                ('poll', models.ForeignKey(blank=True, to='attachments.Poll', null=True)),
                ('review', models.ForeignKey(blank=True, to='attachments.Review', null=True)),
            ],
            options={
                'ordering': ['-position'],
                'verbose_name_plural': 'Stories',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
    ]
