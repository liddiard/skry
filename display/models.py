from django.db import models
from django.contrib.sites.models import Site


class CardSize(models.Model):
    """A preset dimension choice for a Story's Card image."""

    width = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()

    def area(self):
        return width * height

    def aspect_ratio(self):
        return float(self.width) / self.height

    def __str__(self):
        return "%dx%d" % (self.width, self.height)


class Stylesheet(models.Model):
    """A CSS file, which may be a library, to include in a Template.

    A common use case is to support Templates that use libraries like Twitter
    Bootstrap or Zurb Foundation.
    """

    name = models.CharField(max_length=64, unique=True)
    file = models.FileField(upload_to='display/stylesheet')

    def __str__(self):
        return self.name


class Script(models.Model):
    """A JavaScript file, which may be a library, to include in a Template.

    A common use case is to support Templates that use libraries like
    AngularJS, React, or jQuery plugins.
    """

    name = models.CharField(max_length=64, unique=True)
    file = models.FileField(upload_to='display/script')

    def __str__(self):
        return self.name


class Template(models.Model):
    """A reusable layout for Pages."""

    name = models.CharField(max_length=64, unique=True)
    file = models.FileField(upload_to='display/template')
    stylesheets = models.ManyToManyField('Stylesheet', blank=True,
                                         help_text='Stylesheets to include '
                                                   'with this template.')
    scripts = models.ManyToManyField('Script', blank=True,
                                     help_text='Stylesheets to include with '
                                               'this template.')
    sites = models.ManyToManyField(Site)

    def __str__(self):
        return self.name
