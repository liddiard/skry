# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_image_pollchoice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.TextField(blank=True)),
                ('title', models.CharField(max_length=128, null=True, blank=True)),
                ('url', models.URLField()),
                ('credit', models.ManyToManyField(to='news.Author', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('assignment_slug', models.SlugField(max_length=128)),
                ('status', models.PositiveIntegerField(default=1, choices=[(1, b'Draft'), (2, b'First editing'), (3, b'Second editing'), (4, b'Rimming'), (5, b'Slotting'), (6, b'Proofing'), (7, b'Ready to publish')])),
                ('title', models.CharField(max_length=128, blank=True)),
                ('url_slug', models.SlugField(max_length=128, blank=True)),
                ('teaser', models.CharField(max_length=128, blank=True)),
                ('subhead', models.CharField(max_length=128, blank=True)),
                ('body', models.TextField()),
                ('template', models.ForeignKey(to='news.Template', to_field='id')),
                ('position', models.PositiveIntegerField(unique=True, db_index=True)),
                ('tag', models.ForeignKey(to_field='id', blank=True, to='news.Tag', null=True)),
                ('series', models.BooleanField(default=False)),
                ('card', models.ImageField(null=True, upload_to=b'news/article/card/%Y/%m/%d/1x/', blank=True)),
                ('card_2x', models.ImageField(null=True, upload_to=b'news/article/card/%Y/%m/%d/2x/', blank=True)),
                ('card_size', models.ForeignKey(to='news.CardSize', to_field='id')),
                ('card_crop', models.CharField(default=b'c', max_length=1, choices=[(b'c', b'center'), (b't', b'top/left'), (b'b', b'bottom/right')])),
                ('feature_card_image', models.BooleanField(default=True)),
                ('publish_time', models.DateTimeField()),
                ('breaking_duration', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('featured_image', models.ImageField(null=True, upload_to=b'news/article/featured_image/%Y/%m/%d/1x/', blank=True)),
                ('featured_image_2x', models.ImageField(null=True, upload_to=b'news/article/featured_image/%Y/%m/%d/2x/', blank=True)),
                ('featured_video', models.ForeignKey(to_field='id', blank=True, to='news.Video', null=True)),
                ('featured_audio', models.ForeignKey(to_field='id', blank=True, to='news.Audio', null=True)),
                ('review', models.ForeignKey(to_field='id', blank=True, to='news.Review', null=True)),
                ('poll', models.ForeignKey(to_field='id', blank=True, to='news.Poll', null=True)),
                ('author', models.ManyToManyField(to='news.Author', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
