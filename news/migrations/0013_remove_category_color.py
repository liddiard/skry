# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20140519_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='color',
        ),
    ]
