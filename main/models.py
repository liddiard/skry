import pytz
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


CARD_CROP_CHOICES = (
    ('c', 'center'), 
    ('t', 'top/left'), 
    ('b', 'bottom/right')
)


class Author(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    organization = models.CharField(max_length=32, default="Daily Bruin",
                                    blank=True)
    # title = models.CharField(max_length=32, blank=True)
    email = models.EmailField(blank=True)
    twitter = models.CharField(max_length=15, blank=True)
                               # current max handle length
    facebook = models.CharField(max_length=32, blank=True)
    mug = models.ImageField(upload_to='main/mug/%Y', null=True, blank=True)
    bio = models.TextField(blank=True)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Article(models.Model):
    DRAFT = 1
    FIRST_EDITING = 2
    SECOND_EDITING = 3
    RIMMING = 4
    PROOFING = 5
    READY_TO_PUBLISH = 6
    STATUS_CHOICES = (
        (DRAFT, 'draft'),
        (FIRST_EDITING, 'first editing'),
        (SECOND_EDITING, 'second editing'),
        (RIMMING, 'rimming'),
        (PROOFING, 'proofing'),
        (READY_TO_PUBLISH, 'ready to publish')
    )

    # primary content
    title = models.CharField(max_length=128)
    url_slug = models.CharField(max_length=128)
    assignment_slug = models.CharField(max_length=128)
    author = models.ManyToManyField('Author', related_name='main_article', 
                                    null=True, blank=True)
    subhead = models.CharField(max_length=128)
    teaser = models.CharField(max_length=128)
    status = models.PositiveIntegerField(choices=STATUS_CHOICES)
    body = models.TextField()
    template = models.ForeignKey('Template') # TODO: add default

    # organization
    position = models.PositiveIntegerField(unique=True, db_index=True)
    category = models.ForeignKey('Category')
    tags = models.ManyToManyField('Tag', null=True, blank=True)

    # card
    card = models.ImageField(upload_to='main/article/card/%Y/%m/%d/1x/', 
                             null=True, blank=True)
    card_2x = models.ImageField(upload_to='main/article/card/%Y/%m/%d/2x/', 
                                null=True, blank=True)
    card_size = models.ForeignKey('CardSize')
    card_crop = models.CharField(max_length=1, choices=CARD_CROP_CHOICES, 
                                default='c')
    feature_card_image = models.BooleanField(default=True)

    # dates and times
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    publish_time = models.DateTimeField()
    breaking_duration = models.PositiveIntegerField(default=0)

    # linked media
    featured_image = models.ImageField(upload_to='main/article/featured_image/'
                                       '%Y/%m/%d/1x/', null=True, blank=True)
    featured_image_2x = models.ImageField(upload_to='main/article/'
                                          'featured_image/%Y/%m/%d/2x/', 
                                          null=True, blank=True)
    featured_video = models.ForeignKey('Video', null=True, blank=True)
    featured_audio = models.ForeignKey('Audio', null=True, blank=True)
    review = models.ForeignKey('Review', null=True, blank=True)
    # social_media_post = models.OneToOneField('scheduler.SMPost', null=True, 
    #                                          blank=True)

    def __unicode__(self):
        return self.assignment_slug


class CardSize(models.Model):
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()

    def __unicode__(self):
        return "%dx%d" % (self.width, self.height)


class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True)
    name = models.CharField(max_length=32, unique=True)
    default_card = models.ImageField(upload_to='main/category/default_card/1x/')
    default_card_2x = models.ImageField(upload_to='main/category/default_card/'
                                        '2x/') 
    default_card_crop = models.CharField(max_length=1, 
                                         choices=CARD_CROP_CHOICES, 
                                         default='c')

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True)
    slug = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name


class Template(models.Model):
    filename = models.CharField(max_length=64, unique=True)
    verbose_name = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return "%s (%s)" % self.verbose_name, self.filename


class Page(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True)
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    template = models.ForeignKey('Template')
    body = models.TextField()

    def __unicode__(self):
        return self.title


class Media(models.Model):
    caption = models.TextField()

    class Meta:
        abstract = True


class Image(Media):
    image = models.ImageField(upload_to='main/image/%Y/%m/%d/original/')
    image_full = models.ImageField(upload_to='main/image/%Y/%m/%d/full/1x/')
    image_full_2x = models.ImageField(upload_to='main/image/%Y/%m/%d/full/2x/')
    image_float = models.ImageField(upload_to='main/image/%Y/%m/%d/float/1x/')
    image_float_2x = models.ImageField(upload_to='main/image/%Y/%m/%d/float/'
                                       '2x/')
    credit = models.ManyToManyField('Author', related_name='main_image', 
                                    blank=True, null=True)

    def __unicode__(self):
        return self.image # TODO: check if needs str() coercion


class Video(Media):
    title = models.CharField(max_length=128, blank=True, null=True)
    url = models.URLField()
    credit = models.ManyToManyField('Author', related_name='main_video', 
                                    blank=True, null=True)

    def __unicode__(self):
        return self.title


class Audio(Media):
    title = models.CharField(max_length=128, blank=True, null=True)
    mp3 = models.FileField(upload_to='main/audio/%Y/%m/%d/mp3/')
    ogg = models.FileField(uplaod_to='main/audio/%Y/%m/%d/ogg/')
    credit = models.ManyToManyField('Author', related_name='main_audio', 
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
    question = models.ForeignKey('Question')
    choice = models.CharField(max_length=128)
    votes = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.choice
