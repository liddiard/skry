# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0002_auto_20150501_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='is_open',
            field=models.BooleanField(default=True, help_text=b'Whether or not the poll is currently accepting new responses.'),
        ),
        migrations.AlterField(
            model_name='review',
            name='item',
            field=models.CharField(help_text=b'The item being reviewed.', max_length=64),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, help_text=b'Rating between zero and ten.', null=True, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='video',
            name='youtube_id',
            field=models.CharField(help_text=b'The unique ID of this video on YouTube, found in the URL, probably around eleven characters and composed of numbers and letters.', max_length=16),
        ),
    ]
