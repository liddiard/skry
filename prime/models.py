from django.db import models
from django.utils.text import slugify

# Create your models here.
class Issue(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    release_date = models.DateField()

class Article(models.Model):
    __upload_path = "prime"

    title = models.CharField(max_length=64)
    lead_photo = models.ImageField(upload_to=__upload_path)
    author = models.ForeignKey('main.Author')
    body = models.TextField()
    issue = models.ForeignKey('Issue')

    def save(self, *args, **kwargs):
        __upload_path = 'prime/%s/lead' % self.issue.slug
        super(Article, self).save(*args, **kwargs)
