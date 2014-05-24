# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_video_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='audio',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]
