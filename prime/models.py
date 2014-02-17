from django.db import models
from django.utils.text import slugify

from PIL import Image as PyImage


# utility functions

def createUploadPath(directory, same_model=False):
    def getUploadPath(instance, filename):
        if same_model:
            slug = instance.slug
        else:
            slug = instance.issue.slug
        return "prime/%(issue)s/%(directory)s/%(filename)s" %\
            {'issue': slug, 'directory': directory,
             'filename': filename}
    return getUploadPath

def getLatestIssue():
    return Issue.objects.latest('release_date')


# models

class Issue(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    release_date = models.DateField()
    get_upload_path = createUploadPath('header', same_model=True)
    header_image = models.ImageField(upload_to=get_upload_path, blank=True,
                                     null=True)

    class Meta:
        ordering = ['release_date']

    def __unicode__(self):
        return self.name

class Article(models.Model):
    issue = models.ForeignKey('Issue', default=None, null=True, blank=True)
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    get_upload_path = createUploadPath('lead')
    lead_photo = models.ImageField(upload_to=get_upload_path)
    teaser = models.CharField(max_length=200)
    author = models.ManyToManyField('main.Author')
    body = models.TextField(blank=True)
    redirect = models.URLField(blank=True)
    position = models.PositiveIntegerField(default=0)
    
    def getPrettyAuthors(self):
        return ' and '.join([str(a) for a in self.author])

    def __unicode__(self):
        return self.title

class Image(models.Model):
    get_upload_path = createUploadPath('article')
    image = models.ImageField(upload_to=get_upload_path)
    issue = models.ForeignKey('Issue', default=None, null=True, blank=True)
    author = models.ForeignKey('main.Author', null=True, blank=True)
    caption = models.TextField(blank=True)

    __original_image = None

    def __init__(self, *args, **kwargs):
        super(Image, self).__init__(*args, **kwargs)
        self.__original_image = self.image

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.image != self.__original_image:
            size = 500, 1000
            super(Image, self).save(force_insert, force_update, *args, **kwargs)
            image = PyImage.open(self.image)
            image.thumbnail(size, PyImage.ANTIALIAS)
            image.save(self.image.path)
        else:
            super(Image, self).save(force_insert, force_update, *args, **kwargs)
        self.__original_image = self.image

    def __unicode__(self):
        return "%s photo by %s (%s...)" % (self.issue, self.author,
                                           self.caption[0:50])

class PDF(models.Model):
    get_upload_path_pdf = createUploadPath('pdf')
    get_upload_path_pdf_image = createUploadPath('pdf_image')
    pdf = models.FileField(upload_to=get_upload_path_pdf)
    image = models.ImageField(upload_to=get_upload_path_pdf_image)
    issue = models.OneToOneField(Issue)

    def __unicode__(self):
        return "%s PDF" % self.issue
