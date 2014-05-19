# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.TextField(blank=True)),
                ('title', models.CharField(max_length=128, null=True, blank=True)),
                ('mp3', models.FileField(upload_to=b'news/audio/%Y/%m/%d/mp3/')),
                ('ogg', models.FileField(upload_to=b'news/audio/%Y/%m/%d/ogg/')),
                ('credit', models.ManyToManyField(to='news.Author', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
