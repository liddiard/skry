# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150415_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='phone',
            field=models.CharField(max_length=12, blank=True),
        ),
    ]
