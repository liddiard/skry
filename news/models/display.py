from django.db import models


class CardSize(models.Model):
    """A preset dimension choice for a Story's Card image."""


    width = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()

    def area(self):
        return width * height

    def aspect_ratio(self):
        return float(self.width) / self.height

    def __unicode__(self):
        return "%dx%d" % (self.width, self.height)


class IncludeCSS(models.Model):
    """A CSS file, which may be a library, to include in a Template.

    A common use case is to support Templates that use either Twitter
    Bootstrap or Zurb Foundation, or to include another common stylesheet
    shared among a group of pages.
    """

    name = models.CharField(max_length=32, unique=True)
    filename = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return self.name


class Template(models.Model):
    """A reusable layout for Pages."""

    filename = models.CharField(max_length=64, unique=True)
    verbose_name = models.CharField(max_length=64, unique=True)
    include_css = models.ManyToManyField('IncludeCSS', blank=True)

    def __unicode__(self):
        return "%s (%s)" % (self.verbose_name, self.filename)
