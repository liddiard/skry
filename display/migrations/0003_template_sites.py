# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('display', '0002_auto_20150505_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='sites',
            field=models.ManyToManyField(to='sites.Site'),
        ),
    ]
