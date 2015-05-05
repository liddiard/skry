# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0003_auto_20150421_1642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='home',
            new_name='home_team',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='opposing',
            new_name='opposing_team',
        ),
        migrations.AlterField(
            model_name='game',
            name='date',
            field=models.DateField(help_text=b'Date on which the game happened or will happen.'),
        ),
    ]
