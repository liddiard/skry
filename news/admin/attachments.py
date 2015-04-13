from django.contrib import admin

from ..models import attachments


class ImageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('image', 'credit', 'caption')
        }),
    )

admin.site.register(attachments.Image, ImageAdmin)


class VideoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'youtube_id', 'caption')
        }),
    )

admin.site.register(attachments.Video, VideoAdmin)


class AudioAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'mp3', 'ogg', 'credit', 'caption')
        }),
    )

admin.site.register(attachments.Audio, AudioAdmin)


class ReviewAdmin(admin.ModelAdmin):
    pass

admin.site.register(attachments.Review, ReviewAdmin)


class PollAdmin(admin.ModelAdmin):
    list_display = ['question', 'is_open']

admin.site.register(attachments.Poll, PollAdmin)


class PollChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice', 'votes', 'question']

admin.site.register(attachments.PollChoice, PollChoiceAdmin)
