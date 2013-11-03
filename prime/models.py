from django.db import models
from django.utils.text import slugify

# Create your models here.
class Issue(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    release_date = models.DateField()

    def __unicode__(self):
        return self.name

class Article(models.Model):
    def getUploadPath(instance, filename):
        return "prime/%s/lead/%s" % (instance.issue.slug, filename)

    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    lead_photo = models.ImageField(upload_to=getUploadPath)
    author = models.ForeignKey('main.Author')
    body = models.TextField()
    issue = models.ForeignKey('Issue')

    def __unicode__(self):
        return self.title
