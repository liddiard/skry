from django.db import models
from django.utils.text import slugify

def createUploadPath(directory):
    def getUploadPath(instance, filename):
        return "prime/%(issue)s/%(directory)s/%(filename)s" %\
            {'issue': instance.issue.slug, 'directory': directory,
             'filename': filename}
    return getUploadPath

def getLatestIssue():
    return Issue.objects.latest('release_date')

class Issue(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    release_date = models.DateField()

    class Meta:
        ordering = ['release_date']

    def __unicode__(self):
        return self.name

class Article(models.Model):
    getUploadPath = createUploadPath('lead')
    issue = models.ForeignKey('Issue', default=getLatestIssue)
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    lead_photo = models.ImageField(upload_to=getUploadPath)
    author = models.ForeignKey('main.Author')
    body = models.TextField()
    position = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.title

class Image(models.Model):
    getUploadPath = createUploadPath('article')
    image = models.ImageField(upload_to=getUploadPath)
    issue = models.ForeignKey('Issue', default=getLatestIssue)
    author = models.ForeignKey('main.Author')
    caption = models.TextField(blank=True)

    def __unicode__(self):
        return "%s photo by %s (%s...)" % (self.issue, self.author,
                                           self.caption[0:50])
