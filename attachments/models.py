from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator
from sorl.thumbnail import get_thumbnail

from authors.models import Organization


class Media(models.Model):
    """A piece of content which has a main component and may have associated
    Authors and a caption."""

    caption = models.TextField(blank=True)

    @property
    def credit(self):
        """Forces child classes to define a "credit" attribute."""

        raise NotImplementedError('Models which inherit from this class must '
                                  'define a "credit" attribute which is a '
                                  'ManyToManyField of authors.Author.')

    def is_courtesy(self):
        """Checks if this Media is courtesy of another organization.

        Returns True if any of the Authors of the Media is not a member of
        this organization."""

        this_organization = Organization.objects.get(pk=1)
        for author in self.credit.all():
            if author.organization != this_organization:
                return True
        return False


    class Meta:
        abstract = True


class Image(Media):
    """An image of any type, including photos, illustrations, and graphics."""

    file = models.ImageField(upload_to='attachments/image/%Y/%m/%d')
    credit = models.ManyToManyField('authors.Author', related_name='news_image',
                                    blank=True)

    # ForeignKey to multiple types of ArtRequest models
    # cf. http://stackoverflow.com/a/6336509
    request_models = models.Q(app_label='requests', model='photorequest') | \
                     models.Q(app_label='requests',
                              model='graphicrequest') | \
                     models.Q(app_label='requests',
                              model='illustrationrequest')
    content_type = models.ForeignKey(ContentType,
                                     limit_choices_to=request_models,
                                     null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def get_image_at_resolution(self, resolution, crop='center', quality=90):
        return get_thumbnail(self.file, resolution, crop=crop,
                             quality=quality).url

    def aspect_ratio(self):
        return float(self.image.width) / self.image.height

    def __str__(self):
        return self.file.name


class Video(Media):
    """A video from YouTube with associated metadata."""

    title = models.CharField(max_length=128)
    youtube_id = models.CharField(max_length=16,
                                  help_text='The unique ID of this video on '
                                  'YouTube, found in the URL, probably around '
                                  'eleven characters and composed of numbers '
                                  'and letters.')
    credit = models.ManyToManyField('authors.Author', related_name='news_video',
                                    blank=True)

    def __str__(self):
        return self.title


class Audio(Media):
    """A self-hosted audio piece with associated metadata."""

    title = models.CharField(max_length=128)
    file = models.FileField(upload_to='attachments/audio/%Y/%m/%d')
    credit = models.ManyToManyField('authors.Author', related_name='news_audio',
                                    blank=True)

    class Meta:
        verbose_name_plural = "Audio"

    def __str__(self):
        return self.title


class Review(models.Model):
    """An editorial rating.

    Examples include movies, albums, and restaurants.
    """

    item = models.CharField(max_length=64, help_text='The item being '
                                                     'reviewed.')
    line_1 = models.CharField(max_length=128, blank=True)
    line_2 = models.CharField(max_length=128, blank=True)
    rating = models.PositiveSmallIntegerField(validators=
                                              [MaxValueValidator(10)],
                                              null=True, blank=True,
                                              help_text='Rating between '
                                                        'zero and ten.')

    def __str__(self):
        return self.item


class Poll(models.Model):
    """A poll question for consumer interaction."""

    question = models.CharField(max_length=128)
    is_open = models.BooleanField(default=True, help_text='Whether or not '
                                                'the poll is currently '
                                                'accepting new responses.')

    def __str__(self):
        return self.question


class PollChoice(models.Model):
    """A selection option for a Poll."""

    question = models.ForeignKey('Poll')
    text = models.CharField(max_length=128)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "[%s...] %s" % (self.question.question[:20], self.text)
