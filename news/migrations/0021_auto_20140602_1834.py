# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0020_auto_20140602_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='card_crop',
            field=models.CharField(default=b'cc', max_length=2, choices=[(b'cc', b'center center'), (b'cl', b'center left'), (b'cl', b'center right'), (b'tl', b'top left'), (b'tc', b'top center'), (b'tr', b'top right'), (b'bl', b'bottom left'), (b'bc', b'bottom center'), (b'br', b'bottom right')]),
        ),
    ]
