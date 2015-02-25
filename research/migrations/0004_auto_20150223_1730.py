# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0003_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(null=True, upload_to=b'research/post/featured_image', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='teaser',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]
