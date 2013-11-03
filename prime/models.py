from django.db import models

# Create your models here.
class Issue(models.Model):
    name = models.CharField(max_length=32)
    release_date = models.DateField()

class Article(models.Model):
    title = models.CharField(max_length=64)
    cover_photo = models.ImageField()
    author = models.CharField(max_length=32) # TODO: ForeignKey to main app
    body = models.TextField()
    issue = models.ForeignKey('Issue')

