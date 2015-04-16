# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('attachments', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='credit',
            field=models.ManyToManyField(related_name='news_video', to='core.Author', blank=True),
        ),
        migrations.AddField(
            model_name='pollchoice',
            name='question',
            field=models.ForeignKey(to='attachments.Poll'),
        ),
        migrations.AddField(
            model_name='image',
            name='credit',
            field=models.ManyToManyField(related_name='news_image', to='core.Author', blank=True),
        ),
        migrations.AddField(
            model_name='image',
            name='request_type',
            field=models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='audio',
            name='credit',
            field=models.ManyToManyField(related_name='news_audio', to='core.Author', blank=True),
        ),
    ]
