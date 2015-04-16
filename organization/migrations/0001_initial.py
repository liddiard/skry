# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('slug', models.SlugField(unique=True, max_length=32)),
                ('description', models.CharField(max_length=128, blank=True)),
                ('default_card', models.ImageField(upload_to=b'organization/section/default_card')),
                ('default_card_focus', models.CharField(default=b'cc', max_length=2, choices=[(b'cc', b'center center'), (b'cl', b'center left'), (b'cr', b'center right'), (b'tl', b'top left'), (b'tc', b'top center'), (b'tr', b'top right'), (b'bl', b'bottom left'), (b'bc', b'bottom center'), (b'br', b'bottom right')])),
                ('twitter', models.CharField(max_length=15, blank=True)),
                ('facebook', models.CharField(max_length=32, blank=True)),
                ('profile_image', models.ImageField(upload_to=b'organization/section/profile_image', blank=True)),
                ('position', models.PositiveIntegerField()),
                ('parent', models.ForeignKey(blank=True, to='organization.Section', null=True)),
                ('sites', models.ManyToManyField(to='sites.Site')),
            ],
            options={
                'ordering': ['-position'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('slug', models.SlugField(unique=True, max_length=32)),
                ('description', models.TextField(blank=True)),
                ('series', models.BooleanField(default=False)),
                ('sites', models.ManyToManyField(to='sites.Site')),
            ],
        ),
    ]
