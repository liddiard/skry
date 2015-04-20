from datetime import timedelta

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.utils.timezone import now as django_now


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
    Audio piece, a Poll, etc.
    """

    # primary content
    assignment_slug = models.CharField(max_length=64)
    status = models.ForeignKey('Status')
    title = models.CharField(max_length=128, blank=True)
    url_slug = models.SlugField(max_length=128, blank=True)
    authors = models.ManyToManyField('authors.Author',
                                     related_name='news_story', blank=True)
    teaser = models.CharField(max_length=128, blank=True)
    subhead = models.CharField(max_length=128, blank=True)
    body = models.TextField(blank=True)
    alternate_template = models.ForeignKey('display.Template', blank=True,
                                           null=True)

    # planning
    summary = models.TextField(blank=True)
    angle = models.TextField(blank=True)
    sources = models.TextField(blank=True)
    late_run = models.BooleanField(default=False)

    # organization
    position = models.PositiveIntegerField(unique=True, db_index=True)
    sections = models.ManyToManyField('organization.Section', blank=True)
    tags = models.ManyToManyField('organization.Tag', blank=True)
    sites = models.ManyToManyField(Site)

    # card
    card = models.ForeignKey('attachments.Image', null=True, blank=True,
                             related_name='news_article_card')
    card_size = models.ForeignKey('display.CardSize')
    card_focus = models.CharField(max_length=2,
                                  choices=settings.IMAGE_FOCUS_CHOICES,
                                  default='cc')
    feature_card_image = models.BooleanField(default=True)

    # dates and times
    publish_time = models.DateTimeField()
    breaking_duration = models.PositiveSmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    # linked media
    featured_image = models.ForeignKey('attachments.Image', null=True,
                                       blank=True,
                                    related_name='news_article_featured_image')
    featured_video = models.ForeignKey('attachments.Video', null=True,
                                       blank=True)
    featured_audio = models.ForeignKey('attachments.Audio', null=True,
                                       blank=True)
    review = models.ForeignKey('attachments.Review', null=True, blank=True)
    poll = models.ForeignKey('attachments.Poll', null=True, blank=True)
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
                self.publish_time < django_now())

    def is_breaking(self):
        """Whether or not the article is currently breaking news"""

        return (self.publish_time + timedelta(hours=self.breaking_duration) >
                django_now())

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
    slug = models.SlugField(max_length=128)
    alternate_template = models.ForeignKey('display.Template', null=True,
                                           blank=True)
    body = models.TextField(blank=True)
    site = models.ForeignKey(Site)

    class Meta:
        unique_together = ('parent', 'slug')

    def __unicode__(self):
        return self.title
