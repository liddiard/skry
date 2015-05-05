# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internalcomment',
            name='user',
            field=models.ForeignKey(help_text=b'User who posted this comment.', to=settings.AUTH_USER_MODEL),
        ),
    ]
