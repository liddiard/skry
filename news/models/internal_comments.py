from django.db import models
from django.contrib.auth.models import User


class InternalComment(models.Model):
    """An internal (not public facing) comment.

    Can be used to inquire about an aspect of a piece of content.
    """

    user = models.ForeignKey(User)
    time_posted = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        abstract = True

    def __unicode__(self):
        return "%s at %s" % (self.user, self.time_posted)


class StoryComment(InternalComment):
    story = models.ForeignKey('Story')

    def __unicode__(self):
        return "%s on %s at %s" % (self.user, self.story, self.time_posted)


class PhotoRequestComment(InternalComment):
    request = models.ForeignKey('PhotoRequest')

    def __unicode__(self):
        return "%s on %s at %s" % (self.user, self.request, self.time_posted)


class GraphicRequestComment(InternalComment):
    request = models.ForeignKey('GraphicRequest')

    def __unicode__(self):
        return "%s on %s at %s" % (self.user, self.request, self.time_posted)


class IllustrationRequestComment(InternalComment):
    request = models.ForeignKey('IllustrationRequest')

    def __unicode__(self):
        return "%s on %s at %s" % (self.user, self.request, self.time_posted)
