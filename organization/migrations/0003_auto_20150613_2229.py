# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('organization', '0002_auto_20150505_0038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='sites',
        ),
        migrations.AddField(
            model_name='section',
            name='site',
            field=models.ForeignKey(default=1, to='sites.Site'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='section',
            name='slug',
            field=models.SlugField(help_text=b'Used as part of the URL for this section.', max_length=32),
        ),
    ]
