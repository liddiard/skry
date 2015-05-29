from datetime import timedelta

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.sites.models import Site


class UserProfile(models.Model):
    pass


class Status(models.Model):
    """A Story's current state in workflow."""

    name = models.CharField(max_length=32, unique=True)
    position = models.PositiveSmallIntegerField(unique=True)

    class Meta:
        verbose_name_plural = "Statuses"
        ordering = ['position']

    def __unicode__(self):
        return self.name


class Story(models.Model):
    """A standalone piece of content that conveys a message to a consumer.

    Stories can include or be composed entirely of text, an Image, a Video, an
    Audio piece, a Poll, etc. or any combination of the aforementioned.
    """

    # primary content
    assignment_slug = models.CharField(max_length=64,
                                       help_text='Succinct, quasi-unique '
                                       'identifier for this story. Should '
                                       'NOT contain a date, section, or any '
                                       'other information already stored on '
                                       'another story field.')
    status = models.ForeignKey('Status',
                               help_text='Current state in workflow.')
    title = models.CharField(max_length=128, blank=True, help_text='Publicly '
                            'displayed headline.')
    url_slug = models.SlugField(max_length=128, blank=True,
                                help_text='Forms a part of the URL for this '
                                          'story.')
    authors = models.ManyToManyField('authors.Author',
                                     related_name='core_story_authors',
                                     blank=True)
    teaser = models.CharField(max_length=128, blank=True, help_text='Short '
                              'subtext related to the story to encourage '
                              'readers to read the story.')
    subhead = models.CharField(max_length=128, blank=True,
                               help_text='Addtional title that suplements '
                                         'the primary title.')
    body = models.TextField(blank=True)
    alternate_template = models.ForeignKey('display.Template', blank=True,
                                           null=True, help_text='Optional '
                                           'alternate template to use for '
                                           'this story.')

    # planning
    summary = models.TextField(blank=True)
    angle = models.TextField(blank=True)
    sources = models.TextField(blank=True)
    late_run = models.BooleanField(default=False, help_text='Whether or '
                                   'not the story is planned to come in '
                                   'later than stories in the section '
                                   'typically do.')

    # organization
    position = models.PositiveIntegerField(unique=True, db_index=True,
                                           help_text='How this story is '
                                           'ordered relative to other '
                                           'stories.')
    sections = models.ManyToManyField('organization.Section', blank=True)
    tags = models.ManyToManyField('organization.Tag', blank=True)
    sites = models.ManyToManyField(Site)

    # card
    card = models.ForeignKey('attachments.Image', null=True, blank=True,
                             related_name='core_story_card',
                             help_text='Image to display with this story in '
                                       'a story list view.')
    card_size = models.ForeignKey('display.CardSize', help_text='The aspect '
                                  'ratio in which the card should be '
                                  'displayed.')
    card_focus = models.CharField(max_length=2,
                                  choices=settings.IMAGE_FOCUS_CHOICES,
                                  default='cc', help_text='Location of the '
                                  'focal point of the card image.')
    feature_card_image = models.BooleanField(default=True,
                                             help_text='Whether or not the '
                                             'card image should also be '
                                             'displayed as the story\'s '
                                             'featured image.')

    # dates and times
    publish_time = models.DateTimeField()
    breaking_duration = models.PositiveSmallIntegerField(default=0,
                                                         help_text='How long '
                                                         'the story should be '
                                                         'displayed as '
                                                         'breaking news.')
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    # linked media
    featured_image = models.ForeignKey('attachments.Image', null=True,
                                       blank=True,
                                     related_name='core_story_featured_image',
                                       help_text='The most prominent image '
                                       'associated with this story.')
    featured_video = models.ForeignKey('attachments.Video', null=True,
                                       blank=True, help_text='The most '
                                       'prominent video associated with this '
                                       'story.')
    featured_audio = models.ForeignKey('attachments.Audio', null=True,
                                       blank=True, help_text='The most '
                                       'prominent audio associated with this '
                                       'story.')
    review = models.ForeignKey('attachments.Review', null=True, blank=True)
    poll = models.ForeignKey('attachments.Poll', null=True, blank=True)
    game = models.ForeignKey('sports.Game', null=True, blank=True,
                             help_text='Sports game associated with this '
                                       'story.')
    # social_media_post = models.OneToOneField('scheduler.SMPost', null=True,
    #                                          blank=True)

    class Meta:
        verbose_name_plural = "Stories"
        ordering = ['-position']

    def get_featured_image(self):
        """Custom accessor for featured image.

        Needed because the `feature_card_image` field determines whether the
        image stored in the `card` field or the image stored in
        `featured_image` field should be displayed as the 'featured image'
        for an article.
        """

        if self.card and self.feature_card_image:
            return self.card
        else:
            return self.featured_image

    def is_published(self):
        """Returns True if the article's status is 'Ready to publish' and the
        current time is greater than (later than) the publish time.
        """

        return (self.status == Status.objects.last() and
                self.publish_time < timezone.now())

    def is_breaking(self):
        """Whether or not the article is currently breaking news"""

        return (self.publish_time + timedelta(hours=self.breaking_duration) >
                timezone.now())

    def get_path(self):
        """Get the URL path to the article from the website root."""

        return "/%s/%s/" % (self.publish_time.strftime("%Y/%m/%d"),
                            self.url_slug)

    def save(self, *args, **kwargs):
        if self.position is None:
            first_story = Story.objects.first()
            if first_story:
                self.position = first_story.position + 1
            else:
                self.position = 0
        super(Story, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.assignment_slug


class Page(models.Model):
    """A single web page which is completely unrelated to a Story.

    Examples include an about page, a staff page, and an opinion submission
    page.
    """

    parent = models.ForeignKey('self', null=True, blank=True)
    title = models.CharField(max_length=128, blank=True)
    slug = models.SlugField(max_length=128, help_text='Forms part of the '
                                                      'URL for this story.')
    alternate_template = models.ForeignKey('display.Template', null=True,
                                           blank=True, help_text='Optional '
                                           'alternate template to use for '
                                           'this story.')
    body = models.TextField(blank=True)
    site = models.ForeignKey(Site)

    class Meta:
        unique_together = ('parent', 'slug')

    def __unicode__(self):
        return self.title
