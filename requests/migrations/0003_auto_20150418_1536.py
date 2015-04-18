# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0002_auto_20150415_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graphicrequest',
            name='images',
        ),
        migrations.RemoveField(
            model_name='illustrationrequest',
            name='images',
        ),
        migrations.RemoveField(
            model_name='photorequest',
            name='images',
        ),
    ]
