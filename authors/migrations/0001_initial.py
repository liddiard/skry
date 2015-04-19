# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=32, blank=True)),
                ('last_name', models.CharField(max_length=32, blank=True)),
                ('organization', models.CharField(default=b'Daily Bruin', max_length=32, blank=True)),
                ('title', models.CharField(max_length=32, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('phone', models.CharField(max_length=12, blank=True)),
                ('twitter', models.CharField(max_length=15, blank=True)),
                ('mug', models.ImageField(upload_to=b'core/author/mug/%Y', blank=True)),
                ('bio', models.TextField(blank=True)),
                ('user', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
