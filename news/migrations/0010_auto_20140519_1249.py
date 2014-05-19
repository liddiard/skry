# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_page_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='twitter',
            field=models.CharField(default='', max_length=15, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='twitter_profile_image',
            field=models.ImageField(null=True, upload_to=b'news/category/twitter_profile/', blank=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='category',
            name='default_card_2x',
        ),
        migrations.AlterField(
            model_name='category',
            name='default_card',
            field=models.ImageField(upload_to=b'news/category/default_card/'),
        ),
    ]
