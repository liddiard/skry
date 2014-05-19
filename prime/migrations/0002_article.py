# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import prime.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '__first__'),
        ('prime', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('issue', models.ForeignKey(default=None, to_field='id', blank=True, to='prime.Issue', null=True)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=128)),
                ('lead_photo', models.ImageField(upload_to=prime.models.get_lead_photo_upload_path)),
                ('teaser', models.CharField(max_length=200)),
                ('body', models.TextField(blank=True)),
                ('redirect', models.URLField(blank=True)),
                ('position', models.PositiveIntegerField(default=0)),
                ('author', models.ManyToManyField(to='news.Author')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
