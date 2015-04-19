from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Author(models.Model):
    """A distinct person or group of people which creates a piece of
    content."""

    user = models.OneToOneField(User, null=True, blank=True)
    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)
    organization = models.CharField(max_length=32,
                                    default=settings.DEFAULT_ORGANIZATION,
                                    blank=True)
    title = models.CharField(max_length=32, blank=True)
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
