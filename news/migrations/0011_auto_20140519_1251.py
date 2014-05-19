# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20140519_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=b'news/category/profile/', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='facebook',
            field=models.CharField(default='', max_length=32, blank=True),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='category',
            name='twitter_profile_image',
        ),
    ]
