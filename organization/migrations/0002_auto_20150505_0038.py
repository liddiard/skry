# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='default_card',
            field=models.ImageField(help_text=b"Default card for stories in this section that don't specify their own card.", upload_to=b'organization/section/default_card'),
        ),
        migrations.AlterField(
            model_name='section',
            name='default_card_focus',
            field=models.CharField(default=b'cc', help_text=b"Location of the focal point for this section's card image.", max_length=2, choices=[(b'cc', b'center center'), (b'cl', b'center left'), (b'cr', b'center right'), (b'tl', b'top left'), (b'tc', b'top center'), (b'tr', b'top right'), (b'bl', b'bottom left'), (b'bc', b'bottom center'), (b'br', b'bottom right')]),
        ),
        migrations.AlterField(
            model_name='section',
            name='description',
            field=models.TextField(help_text=b'Short description of what this section covers/is about.', blank=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='facebook',
            field=models.CharField(help_text=b'Facebook username for this section. Can be found in the URL.', max_length=32, blank=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='position',
            field=models.PositiveIntegerField(help_text=b'Ordering of this section relative to other sections.'),
        ),
        migrations.AlterField(
            model_name='section',
            name='profile_image',
            field=models.ImageField(help_text=b'Social media profile image for this section.', upload_to=b'organization/section/profile_image', blank=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='slug',
            field=models.SlugField(help_text=b'Used as part of the URL for this section.', unique=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='section',
            name='twitter',
            field=models.CharField(help_text=b'Twitter handle for this section, without an "@" symbol.', max_length=15, blank=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.TextField(help_text=b'Short description of what this tag is about.', blank=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='series',
            field=models.BooleanField(default=False, help_text=b'Whether or not this tag is forms a series.'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(help_text=b'Used as part of the URL for this tag.', unique=True, max_length=32),
        ),
    ]
