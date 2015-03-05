from datetime import datetime

from django.db import models

from . import utils


class CreatedContent(models.Model):
    authors = models.ManyToManyField('news.Author')

    class Meta:
        abstract = True

    def get_pretty_authors(self):
        """
        Creates a comma/'and'-separated list of names for multiple authors in
        AP style format.
        """
        return utils.pretty_list_from_queryset(self.authors.all())


class Post(CreatedContent):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    teaser = models.CharField(max_length=256)
    body = models.TextField()
    published = models.DateTimeField(default=datetime.now)
    featured_image = models.ImageField(upload_to='research/post/'
                                       'featured_image', null=True, blank=True)
    project = models.ForeignKey('Project', null=True, blank=True)

    class Meta:
        ordering = ('-published',)

    def __unicode__(self):
        return self.title


class Project(CreatedContent):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    description = models.TextField()
    published = models.DateTimeField(default=datetime.now)
    featured_image = models.ImageField(upload_to='research/project/'
                                       'featured_image')
    github = models.URLField(blank=True)
    link = models.URLField(blank=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ('-published',)

    def __unicode__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='research/image/%Y/%m/%d/')
    caption = models.TextField(blank=True)

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
