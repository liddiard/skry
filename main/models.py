from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    organization = models.CharField(max_length=32, default="Daily Bruin",
                                    blank=True)
    # title = models.CharField(max_length=32, null=True, blank=True)
    email = models.EmailField(blank=True)
    twitter = models.CharField(max_length=15, blank=True)
                               # current max handle length
    facebook = models.CharField(max_length=32, blank=True)
    mug = models.ImageField(upload_to='mug/%Y', null=True, blank=True)
    bio = models.TextField(blank=True)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
