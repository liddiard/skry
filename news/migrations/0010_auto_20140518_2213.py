# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_page_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_float_2x',
            field=models.ImageField(null=True, upload_to=b'news/image/%Y/%m/%d/float/2x/', blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_full',
            field=models.ImageField(null=True, upload_to=b'news/image/%Y/%m/%d/full/1x/', blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_full_2x',
            field=models.ImageField(null=True, upload_to=b'news/image/%Y/%m/%d/full/2x/', blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_float',
            field=models.ImageField(null=True, upload_to=b'news/image/%Y/%m/%d/float/1x/', blank=True),
        ),
    ]
