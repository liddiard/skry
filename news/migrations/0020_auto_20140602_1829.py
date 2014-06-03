# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0019_category_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='card_crop',
            field=models.CharField(default=b'cc', max_length=1, choices=[(b'cc', b'center center'), (b'cl', b'center left'), (b'cl', b'center right'), (b'tl', b'top left'), (b'tc', b'top center'), (b'tr', b'top right'), (b'bl', b'bottom left'), (b'bc', b'bottom center'), (b'br', b'bottom right')]),
        ),
        migrations.AlterField(
            model_name='category',
            name='default_card_crop',
            field=models.CharField(default=b'c', max_length=1, choices=[(b'cc', b'center center'), (b'cl', b'center left'), (b'cl', b'center right'), (b'tl', b'top left'), (b'tc', b'top center'), (b'tr', b'top right'), (b'bl', b'bottom left'), (b'bc', b'bottom center'), (b'br', b'bottom right')]),
        ),
    ]
