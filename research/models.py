from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    body = models.TextField()
    authors = models.ManyToManyField('news.Author')
    published = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey('Project', null=True, blank=True)

    class Meta:
        ordering = ('-published',)

    def __unicode__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    description = models.TextField()
    authors = models.ManyToManyField('news.Author')
    published = models.DateTimeField(auto_now_add=True)
    featured_image = models.ImageField(upload_to='research/project/'
                                       'featured_image')
    github = models.URLField(blank=True)
    link = models.URLField(blank=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ('-published',)

    def __unicode__(self):
        return self.name
