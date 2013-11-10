from django.db import models
from django.utils.text import slugify

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
    issue = models.ForeignKey('Issue', default=getLatestIssue)
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    get_upload_path = createUploadPath('lead')
    lead_photo = models.ImageField(upload_to=get_upload_path)
    teaser = models.CharField(max_length=200)
    author = models.ForeignKey('main.Author')
    body = models.TextField()
    position = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.title

class Image(models.Model):
    get_upload_path = createUploadPath('article')
    image = models.ImageField(upload_to=get_upload_path)
    issue = models.ForeignKey('Issue', default=getLatestIssue)
    author = models.ForeignKey('main.Author')
    caption = models.TextField(blank=True)

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
