# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0002_auto_20150415_1437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pollchoice',
            old_name='choice',
            new_name='text',
        ),
    ]
