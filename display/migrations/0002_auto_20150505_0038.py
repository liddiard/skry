# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='scripts',
            field=models.ManyToManyField(help_text=b'Stylesheets to include with this template.', to='display.Script', blank=True),
        ),
        migrations.AlterField(
            model_name='template',
            name='stylesheets',
            field=models.ManyToManyField(help_text=b'Stylesheets to include with this template.', to='display.Stylesheet', blank=True),
        ),
    ]
