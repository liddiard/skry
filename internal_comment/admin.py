from django.contrib import admin

from . import models


class StoryCommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'story', 'time_posted']

admin.site.register(models.StoryComment, StoryCommentAdmin)
