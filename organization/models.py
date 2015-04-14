from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site


class Section(models.Model):
    """A distinct, recurring classification for a group of Stories.

    It is recommended that Sections bear resemblance to internal departments
    and/or beats which regularly create Stories.
    """

    parent = models.ForeignKey('self', null=True, blank=True)
    name = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(max_length=32, unique=True)
    description = models.CharField(max_length=128, blank=True)
    default_card = models.ImageField(upload_to='news/section/default_card/')
    default_card_focus = models.CharField(max_length=2,
                                          choices=settings.IMAGE_FOCUS_CHOICES,
                                          default='cc')
    twitter = models.CharField(max_length=15, blank=True)
    facebook = models.CharField(max_length=32, blank=True)
    profile_image = models.ImageField(upload_to='news/section/profile/',
                                      null=True, blank=True)
    position = models.PositiveIntegerField()
    sites = models.ManyToManyField(Site)

    class Meta:
        ordering = ['-position']

    def get_path(self):
        path_components = []
        section = self
        while section is not None:
            path_components.append(section.slug)
            section = section.parent
        return "/" + "/".join(path_components[::-1]) + "/"

    def get_top_level_parent(self):
        """Get the highest section in the hierarchy under which this section
        resides. If the section has no parent, return self.
        """

        section = self
        while section.parent is not None:
            section = section.parent
        return section

    def hierarchy_level(self):
        """Returns the number of levels deep the section is nested, where zero
        is the top level.
        """

        level = 0
        section = self
        while section.parent is not None:
            level += 1
            section = section.parent
        return level

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    """A distinct classification for groups of Stories around a theme.

    Tags may be used for groups of stories for a one-time event or for
    recurring coverage around a theme which is not prominent enough to warrant
    its own Section.
    """

    name = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(max_length=32, unique=True)
    description = models.TextField(blank=True)
    series = models.BooleanField(default=False)
    sites = models.ManyToManyField(Site)

    def __unicode__(self):
        return self.name
