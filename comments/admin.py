import reversion
from reversion.admin import VersionAdmin
from django.contrib import admin

from . import models


class InternalCommentAdmin(VersionAdmin):
    list_display = ['user', 'content_object', 'time_posted']

admin.site.register(models.InternalComment, InternalCommentAdmin)
