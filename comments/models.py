from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class InternalComment(models.Model):
    """An internal (not public facing) comment.

    Can be used to inquire about an aspect of a piece of content.
    """

    user = models.ForeignKey(User)
    time_posted = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    # ForeignKey to multiple commentable models
    # cf. http://stackoverflow.com/a/6336509
    commentable_models = models.Q(app_label='core', model='story') | \
                         models.Q(app_label='requests',
                                  model='photorequest') | \
                         models.Q(app_label='requests',
                                  model='graphicrequest') | \
                         models.Q(app_label='requests',
                                  model='illustrationrequest')
    content_type = models.ForeignKey(ContentType,
                                     limit_choices_to=commentable_models)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return "%s on %s at %s" % (self.user, self.content_object,
                                   self.time_posted)
