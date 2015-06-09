import reversion
from django.contrib import admin

from . import models


class InternalCommentAdmin(reversion.VersionAdmin):
    list_display = ['user', 'content_object', 'time_posted']

admin.site.register(models.InternalComment, InternalCommentAdmin)
