# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_position_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='twitter',
            field=models.CharField(help_text=b'Twitter handle, without an "@" symbol.', max_length=15, blank=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='description',
            field=models.CharField(help_text=b'What the individual in this position is responsible for.', max_length=128, blank=True),
        ),
    ]
