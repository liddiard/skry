from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Author(models.Model):
    """A distinct person or group of people which creates a piece of
    content."""

    user = models.OneToOneField(User, null=True, blank=True)
    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)
    organization = models.ForeignKey('Organization', null=True, blank=True)
    positions = models.ManyToManyField('Position', through='Job', blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=12, blank=True)
    twitter = models.CharField(max_length=15, blank=True)
                               # current max handle length
    mug = models.ImageField(upload_to='core/author/mug/%Y', blank=True)
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


class Organization(models.Model):
    """A group of people under a single name."""

    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class Position(models.Model):
    """A position of employment that can be held by an Author."""

    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name


class Job(models.Model):
    """A specific instance of an Author holding a Position for a period of
    time.

    Custom through model for Author.positions."""

    author = models.ForeignKey('Author')
    position = models.ForeignKey('Position')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
