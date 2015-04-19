# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraphicRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instructions', models.TextField(blank=True)),
                ('external_link', models.URLField(blank=True)),
                ('assignees', models.ManyToManyField(to='authors.Author', blank=True)),
                ('story', models.ForeignKey(to='core.Story')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IllustrationRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instructions', models.TextField(blank=True)),
                ('external_link', models.URLField(blank=True)),
                ('assignees', models.ManyToManyField(to='authors.Author', blank=True)),
                ('story', models.ForeignKey(to='core.Story')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PhotoRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instructions', models.TextField(blank=True)),
                ('time', models.DateTimeField(null=True, blank=True)),
                ('location', models.CharField(max_length=64, blank=True)),
                ('subject_info', models.CharField(max_length=64, blank=True)),
                ('assignees', models.ManyToManyField(to='authors.Author', blank=True)),
                ('story', models.ForeignKey(to='core.Story')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
