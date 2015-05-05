# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_story_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='alternate_template',
            field=models.ForeignKey(blank=True, to='display.Template', help_text=b'Optional alternate template to use for this story.', null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(help_text=b'Forms part of the URL for this story.', max_length=128),
        ),
        migrations.AlterField(
            model_name='story',
            name='alternate_template',
            field=models.ForeignKey(blank=True, to='display.Template', help_text=b'Optional alternate template to use for this story.', null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='assignment_slug',
            field=models.CharField(help_text=b'Succinct, quasi-unique identifier for this story. Should NOT contain a date, section, or any other information already stored on another story field.', max_length=64),
        ),
        migrations.AlterField(
            model_name='story',
            name='authors',
            field=models.ManyToManyField(related_name='core_story_authors', to='authors.Author', blank=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='breaking_duration',
            field=models.PositiveSmallIntegerField(default=0, help_text=b'How long the story should be displayed as breaking news.'),
        ),
        migrations.AlterField(
            model_name='story',
            name='card',
            field=models.ForeignKey(related_name='core_story_card', blank=True, to='attachments.Image', help_text=b'Image to display with this story in a story list view.', null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='card_focus',
            field=models.CharField(default=b'cc', help_text=b'Location of the focal point of the card image.', max_length=2, choices=[(b'cc', b'center center'), (b'cl', b'center left'), (b'cr', b'center right'), (b'tl', b'top left'), (b'tc', b'top center'), (b'tr', b'top right'), (b'bl', b'bottom left'), (b'bc', b'bottom center'), (b'br', b'bottom right')]),
        ),
        migrations.AlterField(
            model_name='story',
            name='card_size',
            field=models.ForeignKey(help_text=b'The aspect ratio in which the card should be displayed.', to='display.CardSize'),
        ),
        migrations.AlterField(
            model_name='story',
            name='feature_card_image',
            field=models.BooleanField(default=True, help_text=b"Whether or not the card image should also be displayed as the story's featured image."),
        ),
        migrations.AlterField(
            model_name='story',
            name='featured_audio',
            field=models.ForeignKey(blank=True, to='attachments.Audio', help_text=b'The most prominent audio associated with this story.', null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='featured_image',
            field=models.ForeignKey(related_name='core_story_featured_image', blank=True, to='attachments.Image', help_text=b'The most prominent image associated with this story.', null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='featured_video',
            field=models.ForeignKey(blank=True, to='attachments.Video', help_text=b'The most prominent video associated with this story.', null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='game',
            field=models.ForeignKey(blank=True, to='sports.Game', help_text=b'Sports game associated with this story.', null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='late_run',
            field=models.BooleanField(default=False, help_text=b'Whether or not the story is planned to come in later than stories in the section typically do.'),
        ),
        migrations.AlterField(
            model_name='story',
            name='position',
            field=models.PositiveIntegerField(help_text=b'How this story is ordered relative to other stories.', unique=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='status',
            field=models.ForeignKey(help_text=b'Current state in workflow.', to='core.Status'),
        ),
        migrations.AlterField(
            model_name='story',
            name='subhead',
            field=models.CharField(help_text=b'Addtional title that suplements the primary title.', max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='teaser',
            field=models.CharField(help_text=b'Short subtext related to the story to encourage readers to read the story.', max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='title',
            field=models.CharField(help_text=b'Publiclydisplayed headline.', max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='url_slug',
            field=models.SlugField(help_text=b'Forms a part of the URL for this story.', max_length=128, blank=True),
        ),
    ]
