# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150417_1834'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='author',
            new_name='authors',
        ),
    ]
