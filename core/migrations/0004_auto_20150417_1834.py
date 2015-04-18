# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150415_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='late_run',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='story',
            name='breaking_duration',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
