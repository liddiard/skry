# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0003_auto_20150421_1642'),
        ('core', '0002_auto_20150421_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='game',
            field=models.ForeignKey(blank=True, to='sports.Game', null=True),
        ),
    ]
