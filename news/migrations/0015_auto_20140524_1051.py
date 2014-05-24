# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_auto_20140523_0059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='title',
        ),
        migrations.RemoveField(
            model_name='video',
            name='credit',
        ),
    ]
