from django.contrib import admin

from ..models import internal_comments


class StoryCommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'story', 'time_posted']

admin.site.register(internal_comments.StoryComment, StoryCommentAdmin)
