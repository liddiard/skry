from django.db import models


class ArtRequest(models.Model):
    """A request for a piece of art to accompany a Story."""

    story = models.ForeignKey('core.Story')
    assignees = models.ManyToManyField('core.Author', blank=True)
    images = models.ManyToManyField('attachments.Image', blank=True)
    instructions = models.TextField(blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return "Art request for " + self.story


class PhotoRequest(ArtRequest):
    time = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=64, blank=True)
    subject_info = models.CharField(max_length=64, blank=True)

    def __unicode__(self):
        return "Photo for " + self.story


class GraphicRequest(ArtRequest):
    external_link = models.URLField(blank=True)

    def __unicode__(self):
        return "Graphic for " + self.story


class IllustrationRequest(ArtRequest):
    external_link = models.URLField(blank=True)

    def __unicode__(self):
        return "Graphic for " + self.story
