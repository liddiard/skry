# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0001_initial'),
        ('news', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=128)),
                ('body', models.TextField()),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(to_field='id', blank=True, to='research.Project', null=True)),
                ('authors', models.ManyToManyField(to='news.Author')),
            ],
            options={
                'ordering': (b'-published',),
            },
            bases=(models.Model,),
        ),
    ]
