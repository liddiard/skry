# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_auto_20140524_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
