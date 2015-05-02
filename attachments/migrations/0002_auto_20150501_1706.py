# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='request_type',
            new_name='content_type',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='request_id',
            new_name='object_id',
        ),
    ]
