# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('artist', models.CharField(max_length=64)),
                ('rating', models.IntegerField()),
                ('review_url', models.URLField()),
                ('author', models.ForeignKey(to='news.Author', to_field='id')),
                ('artwork', models.ImageField(upload_to=b'music/')),
                ('spotify_url', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
