# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photorequest',
            name='subject_info',
            field=models.CharField(max_length=64, blank=True),
        ),
    ]
