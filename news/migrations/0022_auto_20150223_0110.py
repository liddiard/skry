# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0021_auto_20140602_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='line_1',
            field=models.CharField(default='', max_length=128, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='alternate_template',
            field=models.ForeignKey(to_field='id', blank=True, to='news.Template', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='line_2',
            field=models.CharField(default='', max_length=128, blank=True),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='review',
            name='info',
        ),
        migrations.RemoveField(
            model_name='page',
            name='template',
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='default_card_crop',
            field=models.CharField(default=b'c', max_length=1, choices=[(b'cc', b'center center'), (b'cl', b'center left'), (b'cr', b'center right'), (b'tl', b'top left'), (b'tc', b'top center'), (b'tr', b'top right'), (b'bl', b'bottom left'), (b'bc', b'bottom center'), (b'br', b'bottom right')]),
        ),
        migrations.AlterField(
            model_name='template',
            name='include_css',
            field=models.CharField(blank=True, unique=True, max_length=8, choices=[(b'fd5', b'Foundation 5'), (b'bs3.1.1', b'Bootstrap 3.1.1'), (b'bs2.3.2', b'Bootstrap 2.3.2')]),
        ),
        migrations.AlterField(
            model_name='page',
            name='body',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='card_crop',
            field=models.CharField(default=b'cc', max_length=2, choices=[(b'cc', b'center center'), (b'cl', b'center left'), (b'cr', b'center right'), (b'tl', b'top left'), (b'tc', b'top center'), (b'tr', b'top right'), (b'bl', b'bottom left'), (b'bc', b'bottom center'), (b'br', b'bottom right')]),
        ),
    ]
