# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphicrequest',
            name='external_link',
            field=models.URLField(help_text=b'Link to an external website for planning associated with this request.', blank=True),
        ),
        migrations.AlterField(
            model_name='illustrationrequest',
            name='external_link',
            field=models.URLField(help_text=b'Link to an external website for planning associated with this request.', blank=True),
        ),
    ]
