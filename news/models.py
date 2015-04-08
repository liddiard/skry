import json
from PIL import Image as PyImage
from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.timezone import now as django_now
from django.forms.models import model_to_dict
from django.template import Context
from django.template.loader import get_template

from sorl.thumbnail import get_thumbnail

from . import utils


CARD_CROP_CHOICES = (
    ('cc', 'center center'),
    ('cl', 'center left'),
    ('cr', 'center right'),
    ('tl', 'top left'),
    ('tc', 'top center'),
    ('tr', 'top right'),
    ('bl', 'bottom left'),
    ('bc', 'bottom center'),
    ('br', 'bottom right'),
)


class Author(models.Model):
    """A distinct person or group of people which creates a piece of
    content."""

    user = models.ForeignKey(User, null=True, blank=True)
    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)
    organization = models.CharField(max_length=32,
                                    default=settings.DEFAULT_ORGANIZATION,
                                    blank=True)
    title = models.CharField(max_length=32, blank=True)
    email = models.EmailField(blank=True)
    twitter = models.CharField(max_length=15, blank=True)
                               # current max handle length
    mug = models.ImageField(upload_to='news/mug/%Y', null=True, blank=True)
    bio = models.TextField(blank=True)

    def full_name(self):
        if self.first_name or self.last_name:
            return "%s %s" % (self.first_name, self.last_name)
        else:
            return ""

    def __unicode__(self):
        if self.full_name():
            return self.full_name()
        else:
            return self.organization


class Status(models.Model):
    """A Story's current state in workflow."""

    name = models.CharField(max_length=32, unique=True)
    position = models.PositiveSmallIntegerField(unique=True)

    def __unicode(self):
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
    author = models.ManyToManyField('Author', related_name='news_story',
                                    blank=True)
    teaser = models.CharField(max_length=128, blank=True)
    subhead = models.CharField(max_length=128, blank=True)
    body = models.TextField(blank=True)
    alternate_template = models.ForeignKey('Template', blank=True, null=True)

    # planning
    summary = models.TextField(blank=True)
    angle = models.TextField(blank=True)
    sources = models.TextField(blank=True)

    # organization
    position = models.PositiveIntegerField(unique=True, db_index=True)
    categories = models.ManyToManyField('Category', blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    series = models.BooleanField(default=False)

    # card
    card = models.ForeignKey('Image', null=True, blank=True,
                             related_name='news_article_card')
    card_size = models.ForeignKey('CardSize')
    card_crop = models.CharField(max_length=2, choices=CARD_CROP_CHOICES,
                                 default='cc')
    feature_card_image = models.BooleanField(default=True)

    # dates and times
    publish_time = models.DateTimeField()
    breaking_duration = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    # linked media
    featured_image = models.ForeignKey('Image', null=True, blank=True,
                                    related_name='news_article_featured_image')
    featured_video = models.ForeignKey('Video', null=True, blank=True)
    featured_audio = models.ForeignKey('Audio', null=True, blank=True)
    review = models.ForeignKey('Review', null=True, blank=True)
    poll = models.ForeignKey('Poll', null=True, blank=True)
    # social_media_post = models.OneToOneField('scheduler.SMPost', null=True,
    #                                          blank=True)

    class Meta:
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

    def card_html(self):
        """Returns a JSON object containing the HTML for the card.

        NOT a public API method.
        """
        context = Context({'article': self, 'MEDIA_URL': settings.MEDIA_URL})
        template = get_template('news/inc/card.html')
        html = template.render(context)
        response_dict = {'pk': self.pk, 'html': html}
        return response_dict

    def is_published(self):
        """Returns True if the article's status is 'Ready to publish' and the
        current time is greater than (later than) the publish time.
        """

        return (self.status == self.READY_TO_PUBLISH and
                self.publish_time < django_now())

    def is_breaking(self):
        """Whether or not the article is currently breaking news"""

        return (self.publish_time + timedelta(hours=self.breaking_duration) >
                django_now())

    def get_path(self):
        """Get the URL path to the article from the website root."""

        return "/%s/%s/" % (self.publish_time.strftime("%Y/%m/%d"),
                            self.url_slug)

    def get_pretty_authors(self):
        """Creates a comma/'and'-separated list of names for multiple authors
        in AP style format.
        """

        return utils.pretty_list_from_queryset(self.author.all())

    def save(self, *args, **kwargs):
        if self.position is None:
            self.position = Story.objects.first().position + 1
        super(Story, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.assignment_slug


def get_published_articles(): # TODO: cache
    return (Story.objects.filter(status=7)
            .filter(publish_time__lt=django_now()))


class ArtRequest(models.Model):
    """A request for a piece of art to accompany a Story."""

    KIND_CHOICES = (
        ('p', 'photo'),
        ('g', 'graphic'),
        ('i', 'illustration')
    )

    story = models.ForeignKey('Story')
    kind = models.CharField(max_length=1, choices=KIND_CHOICES)
    location = models.TextField(blank=True)
    time = models.DateTimeField(null=True, blank=True)
    instructions = models.TextField(blank=True)
    external_link = models.URLField(blank=True)
    images = models.ManyToManyField('Image', blank=True)

    def __unicode__(self):
        return self.get_kind_display() + " for " + self.story


class InternalStoryComment(models.Model):
    """An internal (not public facing) comment about a Story.

    Can be used to inquire about an aspect of the Story.
    """

    user = models.ForeignKey(User)
    time_posted = models.DateTimeField(auto_now_add=True)
    story = models.ForeignKey('Story')
    text = models.TextField()

    def __unicode__(self):
        return "%s on %s at %s" % (self.user, self.article, self.time_posted)


class CardSize(models.Model):
    """A preset dimension choice for a Story's Card image."""


    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()

    def area(self):
        return width * height

    def aspect_ratio(self):
        return float(self.width) / self.height

    def __unicode__(self):
        return "%dx%d" % (self.width, self.height)


class Category(models.Model):
    """A distinct, recurring classification for a group of Stories.

    It is recommended that Categories bear resemblance to internal departments
    and/or beats which regularly create Stories.
    """

    parent = models.ForeignKey('self', null=True, blank=True)
    name = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(max_length=32, unique=True)
    description = models.CharField(max_length=128, blank=True)
    default_card = models.ImageField(upload_to='news/category/default_card/')
    default_card_crop = models.CharField(max_length=1,
                                         choices=CARD_CROP_CHOICES,
                                         default='c')
    twitter = models.CharField(max_length=15, blank=True)
    facebook = models.CharField(max_length=32, blank=True)
    profile_image = models.ImageField(upload_to='news/category/profile/',
                                      null=True, blank=True)
    position = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['-position']

    def get_path(self):
        path_components = []
        category = self
        while category is not None:
            path_components.append(category.slug)
            category = category.parent
        return "/" + "/".join(path_components[::-1]) + "/"

    def get_top_level_parent(self):
        """Get the highest category in the hierarchy under which this category
        resides. If the category has no parent, return self.
        """

        category = self
        while category.parent is not None:
            category = category.parent
        return category

    def hierarchy_level(self):
        """Returns the number of levels deep the category is nested, where zero
        is the top level.
        """

        level = 0
        category = self
        while category.parent is not None:
            level += 1
            category = category.parent
        return level

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    """A distinct classification for groups of Stories around a theme.

    Tags may be used for groups of stories for a one-time event or for
    recurring coverage around a theme which is not prominent enough to warrant
    a Category.
    """

    name = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(max_length=32, unique=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class IncludeCSS(models.Model):
    """A CSS file, which may be a library, to include in a Template.

    A common use case is to support Templates that use either Twitter
    Bootstrap or Zurb Foundation, or to include another common stylesheet
    shared among a group of pages.
    """

    name = models.CharField(max_length=32, unique=True)
    filename = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return self.name


class Template(models.Model):
    """A reusable layout for Pages."""

    filename = models.CharField(max_length=64, unique=True)
    verbose_name = models.CharField(max_length=64, unique=True)
    include_css = models.ManyToManyField('IncludeCSS', blank=True)

    def __unicode__(self):
        return "%s (%s)" % (self.verbose_name, self.filename)


class Page(models.Model):
    """A single web page which is completely unrelated to a Story.

    Examples include an about page, a staff page, and an opinion submission
    page.
    """

    parent = models.ForeignKey('self', null=True, blank=True)
    title = models.CharField(max_length=128, blank=True)
    slug = models.SlugField(max_length=128)
    alternate_template = models.ForeignKey('Template', null=True, blank=True)
    body = models.TextField(blank=True)

    def __unicode__(self):
        return self.title


# abstract base class
# https://docs.djangoproject.com/en/1.7/topics/db/models/#abstract-base-classes
class Media(models.Model):
    """A piece of content which has a main component and may have associated
    Authors and a caption."""

    caption = models.TextField(blank=True)

    class Meta:
        abstract = True

    def get_pretty_credit(self):
        return utils.pretty_list_from_queryset(self.credit.all())

    def display_courtesy(self):
        first_author = self.credit.first()
        if ((first_author.first_name or first_author.last_name) and not
            first_author.organization):
            return True
        else:
            return False

    def display_organization(self):
        last_author = self.credit.last()
        if (not (last_author.first_name or last_author.last_name) and
            last_author.organization):
            return False
        else:
            return last_author.organization


class Image(Media):
    """An image of any type, including photos, illustrations, and graphics."""

    image = models.ImageField(upload_to='news/image/%Y/%m/%d/original/')
    credit = models.ManyToManyField('Author', related_name='news_image',
                                    blank=True)

    def get_image_at_resolution(self, resolution):
        return get_thumbnail(self.image, resolution).url

    def get_full(self):
        return self.get_image_at_resolution("640")

    def get_float(self):
        return self.get_image_at_resolution("320")

    def aspect_ratio(self):
        return float(self.image.width) / self.image.height

    def __unicode__(self):
        return self.image.name


class Video(Media):
    """A video from YouTube with associated metadata."""

    title = models.CharField(max_length=128)
    youtube_id = models.CharField(max_length=16)
    credit = models.ManyToManyField('Author', related_name='news_video',
                                    blank=True)

    def __unicode__(self):
        return self.title


class Audio(Media):
    """A self-hosted audio piece with associated metadata."""

    title = models.CharField(max_length=128)
    mp3 = models.FileField(upload_to='news/audio/%Y/%m/%d/mp3/')
    ogg = models.FileField(upload_to='news/audio/%Y/%m/%d/ogg/')
    credit = models.ManyToManyField('Author', related_name='news_audio',
                                    blank=True)

    class Meta:
        verbose_name_plural = "Audio"

    def __unicode__(self):
        return self.title


class Review(models.Model):
    """An editorial rating.

    Examples include movies, albums, and restaurants.
    """

    item = models.CharField(max_length=64)
    line_1 = models.CharField(max_length=128, blank=True)
    line_2 = models.CharField(max_length=128, blank=True)
    rating = models.PositiveIntegerField(null=True, blank=True) # TODO: limit to range

    def __unicode__(self):
        return self.item


class Poll(models.Model):
    """A poll question for consumer interaction."""

    question = models.CharField(max_length=128)
    is_open = models.BooleanField(default=True)

    def __unicode__(self):
        return self.question


class PollChoice(models.Model):
    """A selection option for a Poll."""

    question = models.ForeignKey('Poll')
    choice = models.CharField(max_length=128)
    votes = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return "[%s...] %s" % (self.question.question[:20], self.choice)
