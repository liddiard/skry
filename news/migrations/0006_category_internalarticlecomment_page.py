# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0005_article_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternalArticleComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('time_posted', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(to='news.Article', to_field='id')),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('slug', models.SlugField(unique=True, max_length=32)),
                ('color', models.CharField(max_length=6)),
                ('default_card', models.ImageField(upload_to=b'news/category/default_card/1x/')),
                ('default_card_2x', models.ImageField(upload_to=b'news/category/default_card/2x/')),
                ('default_card_crop', models.CharField(default=b'c', max_length=1, choices=[(b'c', b'center'), (b't', b'top/left'), (b'b', b'bottom/right')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=128)),
                ('template', models.ForeignKey(to='news.Template', to_field='id')),
                ('body', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
