# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0003_image_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ManyToManyField(related_name='prime_article', to='news.Author'),
        ),
        migrations.AlterField(
            model_name='image',
            name='author',
            field=models.ForeignKey(related_name='prime_image', blank=True, to='news.Author', null=True),
        ),
    ]
