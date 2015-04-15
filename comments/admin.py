from django.contrib import admin

from . import models


class InternalCommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'content_object', 'time_posted']

admin.site.register(models.InternalComment, InternalCommentAdmin)
