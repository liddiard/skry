# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0017_auto_20140524_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(default='', max_length=128, blank=True),
            preserve_default=False,
        ),
    ]
