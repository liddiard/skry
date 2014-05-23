# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_remove_category_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='youtube_id',
            field=models.CharField(default='', max_length=16),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='video',
            name='url',
        ),
        migrations.AlterField(
            model_name='article',
            name='card_crop',
            field=models.CharField(default=b'c', max_length=1, choices=[(b'c', b'center'), (b't', b'top-left'), (b'b', b'bottom-right')]),
        ),
        migrations.AlterField(
            model_name='article',
            name='assignment_slug',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='category',
            name='default_card_crop',
            field=models.CharField(default=b'c', max_length=1, choices=[(b'c', b'center'), (b't', b'top-left'), (b'b', b'bottom-right')]),
        ),
    ]
