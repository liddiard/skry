# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('display', '0001_initial'),
        ('core', '0001_initial'),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='sections',
            field=models.ManyToManyField(to='organization.Section', blank=True),
        ),
        migrations.AddField(
            model_name='story',
            name='sites',
            field=models.ManyToManyField(to='sites.Site'),
        ),
        migrations.AddField(
            model_name='story',
            name='status',
            field=models.ForeignKey(to='core.Status'),
        ),
        migrations.AddField(
            model_name='story',
            name='tags',
            field=models.ManyToManyField(to='organization.Tag', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='alternate_template',
            field=models.ForeignKey(blank=True, to='display.Template', null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='parent',
            field=models.ForeignKey(blank=True, to='core.Page', null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='site',
            field=models.ForeignKey(to='sites.Site'),
        ),
    ]
