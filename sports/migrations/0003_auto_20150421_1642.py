# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0002_game_sport'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Team',
            new_name='School',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='home_team',
            new_name='home',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='home_team_score',
            new_name='home_score',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='opposing_team',
            new_name='opposing',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='opposing_team_score',
            new_name='opposing_score',
        ),
    ]
