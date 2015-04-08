# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0022_auto_20150223_0110'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-position']},
        ),
        migrations.AlterModelOptions(
            name='audio',
            options={'verbose_name_plural': 'Audio'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-position'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ManyToManyField(related_name='news_article', to='news.Author', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='card',
            field=models.ForeignKey(related_name='news_article_card', blank=True, to='news.Image', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='featured_image',
            field=models.ForeignKey(related_name='news_article_featured_image', blank=True, to='news.Image', null=True),
        ),
        migrations.AlterField(
            model_name='audio',
            name='credit',
            field=models.ManyToManyField(related_name='news_audio', to='news.Author', blank=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='credit',
            field=models.ManyToManyField(related_name='news_image', to='news.Author', blank=True),
        ),
    ]
