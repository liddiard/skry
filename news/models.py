import pytz
from PIL import Image as PyImage
from cStringIO import StringIO
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile


CARD_CROP_CHOICES = (
    ('c', 'center'), 
    ('t', 'top/left'), 
    ('b', 'bottom/right')
)


class Author(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)
    organization = models.CharField(max_length=32, default="Daily Bruin",
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
    assignment_slug = models.SlugField(max_length=128)
    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=DRAFT)
    title = models.CharField(max_length=128, blank=True)
    url_slug = models.SlugField(max_length=128, blank=True)
    author = models.ManyToManyField('Author', related_name='news_article', 
                                    null=True, blank=True)
    teaser = models.CharField(max_length=128, blank=True)
    subhead = models.CharField(max_length=128, blank=True)
    body = models.TextField()
    template = models.ForeignKey('Template') # TODO: add default

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
    featured_image = models.ForeignKey(null=True, blank=True, 
                                       related_name='news_article_featured_'
                                                    'image')
    featured_video = models.ForeignKey('Video', null=True, blank=True)
    featured_audio = models.ForeignKey('Audio', null=True, blank=True)
    review = models.ForeignKey('Review', null=True, blank=True)
    poll = models.ForeignKey('Poll', null=True, blank=True)
    # social_media_post = models.OneToOneField('scheduler.SMPost', null=True, 
    #                                          blank=True)

    def __unicode__(self):
        return self.assignment_slug


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
    color = models.CharField(max_length=6) # hex value
    default_card = models.ImageField(upload_to='news/category/default_card/1x/')
    default_card_2x = models.ImageField(upload_to='news/category/default_card/'
                                        '2x/') 
    default_card_crop = models.CharField(max_length=1, 
                                         choices=CARD_CROP_CHOICES, 
                                         default='c')

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

    class Meta:
        abstract = True


class Image(Media):
    image = models.ImageField(upload_to='news/image/%Y/%m/%d/original/')
    image_full = models.ImageField(upload_to='news/image/%Y/%m/%d/full/1x/',
                                   null=True, blank=True)
    image_full_2x = models.ImageField(upload_to='news/image/%Y/%m/%d/full/2x/',
                                      null=True, blank=True)
    image_float = models.ImageField(upload_to='news/image/%Y/%m/%d/float/1x/',
                                    null=True, blank=True)
    image_float_2x = models.ImageField(upload_to='news/image/%Y/%m/%d/float/'
                                       '2x/', null=True, blank=True)
    image_card = models.ImageField(upload_to='news/image/%Y/%m/%d/card/1x/', 
                                   null=True, blank=True)
    image_card_2x = models.ImageField(upload_to='news/image/%Y/%m/%d/card/2x/', 
                                      null=True, blank=True)
    credit = models.ManyToManyField('Author', related_name='news_image', 
                                    blank=True, null=True)

    def get_full(self):
        if not self.image_full:
            width = settings.IMAGE_DIMENSIONS['full']['width']
            resized = self.resize_to_width(width=width)
            self.image_full = resized
            self.save()
        return self.image_full

    def resize_to_width(self, width):
        img = PyImage.open(self.image)
        wpercent = (width / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((width, hsize), PyImage.ANTIALIAS)
        temp_handle = StringIO()
        image.save(temp_handle, 'JPEG')
        temp_handle.seek(0)
        return img

    def __unicode__(self):
        return self.image.name # TODO: check if needs str() coercion


class Video(Media):
    title = models.CharField(max_length=128, blank=True, null=True)
    url = models.URLField()
    credit = models.ManyToManyField('Author', related_name='news_video', 
                                    blank=True, null=True)

    def __unicode__(self):
        return self.title


class Audio(Media):
    title = models.CharField(max_length=128, blank=True, null=True)
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
