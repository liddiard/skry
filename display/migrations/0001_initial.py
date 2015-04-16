# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardSize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('width', models.PositiveSmallIntegerField()),
                ('height', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
                ('file', models.FileField(upload_to=b'display/script')),
            ],
        ),
        migrations.CreateModel(
            name='Stylesheet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
                ('file', models.FileField(upload_to=b'display/stylesheet')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
                ('file', models.FileField(upload_to=b'display/template')),
                ('scripts', models.ManyToManyField(to='display.Script', blank=True)),
                ('stylesheets', models.ManyToManyField(to='display.Stylesheet', blank=True)),
            ],
        ),
    ]
