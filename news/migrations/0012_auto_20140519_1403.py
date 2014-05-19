# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20140519_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='alternate_template',
            field=models.ForeignKey(to_field='id', blank=True, to='news.Template', null=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='article',
            name='template',
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]
