# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='sport',
            field=models.ForeignKey(default=1, to='sports.Sport'),
            preserve_default=False,
        ),
    ]
