from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site


class Section(models.Model):
    """A distinct, recurring classification for a group of Stories.

    It is recommended that Sections bear resemblance to internal departments
    and/or beats which regularly create Stories.
    """

    parent = models.ForeignKey('self', null=True, blank=True)
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32, help_text='Used as part of the URL '
                                                     'for this section.')
    description = models.TextField(blank=True, help_text='Short description '
                                   'of what this section covers/is about.')
    default_card = models.ImageField(upload_to='organization/section/'
                                     'default_card', help_text='Default card '
                                     'for stories in this section that '
                                     'don\'t specify their own card.')
    default_card_focus = models.CharField(max_length=2,
                                          choices=settings.IMAGE_FOCUS_CHOICES,
                                          default='cc', help_text='Location '
                                          'of the focal point for this '
                                          'section\'s card image.')
    twitter = models.CharField(max_length=15, blank=True, help_text='Twitter '
                               'handle for this section, without an "@" '
                               'symbol.')
    facebook = models.CharField(max_length=32, blank=True,
                                help_text='Facebook username for this '
                                          'section. Can be found in the URL.')
    profile_image = models.ImageField(upload_to='organization/section/'
                                      'profile_image', blank=True,
                                      help_text='Social media profile image '
                                                'for this section.')
    position = models.PositiveIntegerField(help_text='Ordering of this '
                                           'section relative to other '
                                           'sections.')
    site = models.ForeignKey(Site)

    class Meta:
        ordering = ['-position']

    def get_path(self):
        # TODO: remove if unused
        path_components = []
        section = self
        while section is not None:
            path_components.append(section.slug)
            section = section.parent
        return "/" + "/".join(path_components[::-1]) + "/"

    def get_top_level_parent(self):
        # TODO: remove if unused
        """Get the highest section in the hierarchy under which this section
        resides. If the section has no parent, return self.
        """

        section = self
        while section.parent is not None:
            section = section.parent
        return section

    def hierarchy_level(self):
        # TODO: remove if unused
        """Returns the number of levels deep the section is nested, where zero
        is the top level.
        """

        level = 0
        section = self
        while section.parent is not None:
            level += 1
            section = section.parent
        return level

    class Meta:
        # ensure that no two Sections can map to the same URL
        unique_together = ('parent', 'slug')

    def __str__(self):
        return self.name


class Tag(models.Model):
    """A distinct classification for groups of Stories around a theme.

    Tags may be used for groups of stories for a one-time event or for
    recurring coverage around a theme which is not prominent enough to warrant
    its own Section.
    """

    name = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(max_length=32, unique=True, help_text='Used as '
                            'part of the URL for this tag.')
    description = models.TextField(blank=True, help_text='Short description '
                                   'of what this tag is about.')
    series = models.BooleanField(default=False, help_text='Whether or not '
                                 'this tag is forms a series.')
    sites = models.ManyToManyField(Site)

    def __str__(self):
        return self.name
