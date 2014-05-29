# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0018_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='position',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
