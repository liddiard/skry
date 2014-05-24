import json
from PIL import Image as PyImage
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.timezone import now as django_now
from django.forms.models import model_to_dict
from django.template import Context
from django.template.loader import get_template
from django.contrib.humanize.templatetags import humanize

from sorl.thumbnail import get_thumbnail

from .templatetags import markdown
from . import utils


CARD_CROP_CHOICES = (
    ('c', 'center'), 
    ('t', 'top-left'), 
    ('b', 'bottom-right')
)


class Author(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)
    organization = models.CharField(max_length=32, 
                                    default=settings.DEFAULT_ORGANIZATION, 
                                    blank=True)
    # title = models.CharField(max_length=32, blank=True)
    email = models.EmailField(blank=True)
    twitter = models.CharField(max_length=15, blank=True)
                               # current max handle length
    mug = models.ImageField(upload_to='news/mug/%Y', null=True, blank=True)
    bio = models.TextField(blank=True)

    def __unicode__(self):
        if self.first_name:
            return "%s %s" % (self.first_name, self.last_name)
        else:
            return self.organization


class Article(models.Model):
    DRAFT = 1
    FIRST_EDITING = 2
    SECOND_EDITING = 3
    RIMMING = 4
    SLOTTING = 5
    PROOFING = 6
    READY_TO_PUBLISH = 7
    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (FIRST_EDITING, 'First editing'),
        (SECOND_EDITING, 'Second editing'),
        (RIMMING, 'Rimming'),
        (SLOTTING, 'Slotting'),
        (PROOFING, 'Proofing'),
        (READY_TO_PUBLISH, 'Ready to publish')
    )

    # primary content
    assignment_slug = models.CharField(max_length=128)
    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=DRAFT)
    title = models.CharField(max_length=128, blank=True)
    url_slug = models.SlugField(max_length=128, blank=True)
    author = models.ManyToManyField('Author', related_name='news_article', 
                                    null=True, blank=True)
    teaser = models.CharField(max_length=128, blank=True)
    subhead = models.CharField(max_length=128, blank=True)
    body = models.TextField(blank=True)
    alternate_template = models.ForeignKey('Template', blank=True, null=True) 

    # organization
    position = models.PositiveIntegerField(unique=True, db_index=True)
    category = models.ForeignKey('Category')
    tag = models.ForeignKey('Tag', null=True, blank=True)
    series = models.BooleanField(default=False)

    # card
    card = models.ForeignKey('Image', null=True, blank=True, 
                             related_name='news_article_card')
    card_size = models.ForeignKey('CardSize')
    card_crop = models.CharField(max_length=1, choices=CARD_CROP_CHOICES, 
                                 default='c')
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
        """
        Custom accessor for featured image. Needed because the
        `feature_card_image` field determines whether the image stored in the
        `card` field or the image stored in `featured_image` field should be
        displayed as the 'featured image' for an article.
        """
        if self.card and self.feature_card_image:
            return self.card
        else:
            return self.featured_image

    def ajax_json(self):
        """
        Returns a JSON object with all of the public article fields to display 
        on an article template. NOT a public API method.
        """
        article = model_to_dict(self, exclude=['status', 'assignment_slug'])
        featured_image = self.get_featured_image()
        if featured_image:
            template = get_template('news/includes/image.html')
            context = Context({'image': featured_image})
            article['featured_image'] = template.render(context)
        featured_video = self.featured_video
        if featured_video:
            template = get_template('news/includes/video.html')
            context = Context({'video': featured_video})
            article['featured_video'] = template.render(context)
        featured_audio = self.featured_audio
        if featured_audio:
            template = get_template('news/includes/audio.html')
            context = Context({'audio': featured_audio, 
                               'MEDIA_URL': settings.MEDIA_URL})
            article['featured_audio'] = template.render(context)
        if self.author:
            article['author'] = self.get_pretty_authors()
        article['category'] = self.category.name
        article['publish_day'] = humanize.naturalday(self.publish_time)
        article['publish_time'] = humanize.naturaltime(self.publish_time)
        article['body'] = markdown.markdown(self.body)
        article = json.dumps(article, cls=utils.DatetimeEncoder)
        return article

    def is_published(self):
        """
        Returns True if the article's status is 'Ready to publish' and the
        current time is greater than (later than) the publish time.
        """
        return (self.status == self.READY_TO_PUBLISH and
                self.publish_time < django_now())

    def get_path(self):
        """
        Get the URL path to the article from the website root.
        """
        return "/%s/%s/" % (self.publish_time.strftime("%Y/%m/%d"), 
                            self.url_slug)

    def get_pretty_authors(self):
        """
        Creates a comma/'and'-separated list of names for multiple authors in
        the format you would write out a list of items in AP style.
        """
        return utils.pretty_list_from_queryset(self.author.all())

    def __unicode__(self):
        return self.assignment_slug


def get_published_articles(): # TODO: cache
    return (Article.objects.filter(status=7)
            .filter(publish_time__lt=django_now()))


class InternalArticleComment(models.Model):
    user = models.ForeignKey(User)
    time_posted = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey('Article')
    text = models.TextField()

    def __unicode__(self):
        return "%s on %s at %s" % (self.user, self.article, self.time_posted)


class CardSize(models.Model):
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()

    def area(self):
        return width * height

    def __unicode__(self):
        return "%dx%d" % (self.width, self.height)


class Category(models.Model):
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

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(max_length=32, unique=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class Template(models.Model):
    INCLUDE_CSS_CHOICES = (
        ('fd5', 'Foundation 5'),
        ('bs3.1.0', 'Bootstrap 3.1.0'),
        ('bs2.3.2', 'Bootstrap 2.3.2'),
    )
    filename = models.CharField(max_length=64, unique=True)
    verbose_name = models.CharField(max_length=64, unique=True)
    include_css = models.CharField(max_length=8, choices=INCLUDE_CSS_CHOICES, 
                                   unique=True)

    def __unicode__(self):
        return "%s (%s)" % self.verbose_name, self.filename


class Page(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True)
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    template = models.ForeignKey('Template')
    body = models.TextField()

    def __unicode__(self):
        return self.title


# abstract base class
# https://docs.djangoproject.com/en/1.7/topics/db/models/#abstract-base-classes
class Media(models.Model):
    caption = models.TextField(blank=True)

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


    class Meta:
        abstract = True


class Image(Media):
    image = models.ImageField(upload_to='news/image/%Y/%m/%d/original/')
    credit = models.ManyToManyField('Author', related_name='news_image', 
                                    blank=True, null=True)

    def get_image_at_resolution(self, resolution):
        return get_thumbnail(self.image, resolution).url

    def get_full(self):
        return self.get_image_at_resolution("640")

    def get_float(self):
        return self.get_image_at_resolution("320")

    def __unicode__(self):
        return self.image.name # TODO: check if needs str() coercion


class Video(Media):
    title = models.CharField(max_length=128)
    youtube_id = models.CharField(max_length=16)

    def __unicode__(self):
        return self.title


class Audio(Media):
    title = models.CharField(max_length=128)
    mp3 = models.FileField(upload_to='news/audio/%Y/%m/%d/mp3/')
    ogg = models.FileField(upload_to='news/audio/%Y/%m/%d/ogg/')
    credit = models.ManyToManyField('Author', related_name='news_audio', 
                                    blank=True, null=True)

    def __unicode__(self):
        return self.title


class Review(models.Model):
    item = models.CharField(max_length=64)
    info = models.TextField(blank=True)
    rating = models.PositiveIntegerField(null=True, blank=True) # TODO: limit to range

    def __unicode__(self):
        return self.item


class Poll(models.Model):
    question = models.CharField(max_length=128)
    is_open = models.BooleanField(default=True)

    def __unicode__(self):
        return self.question


class PollChoice(models.Model):
    question = models.ForeignKey('Poll')
    choice = models.CharField(max_length=128)
    votes = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.choice
