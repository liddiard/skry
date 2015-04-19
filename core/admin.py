from django.contrib import admin

from . import models


class StatusAdmin(admin.ModelAdmin):
    list_display = ['position', 'name']


admin.site.register(models.Status, StatusAdmin)


class StoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url_slug': ('title',)}
    readonly_fields = ('created', 'last_updated', 'position')
    list_display = ['assignment_slug', 'title', 'publish_time', 'status']
    fieldsets = (
        ('Primary content', {
            'fields': (
                ('assignment_slug', 'status'),
                ('title', 'url_slug'),
                ('author'),
                ('teaser', 'subhead'),
                ('body'),
                ('alternate_template'),
            )
        }),
        ('Organization', {
            'fields': (
                ('sections', 'tags', 'position'),
            )
        }),
        ('Card', {
            'fields': (
                ('card', 'card_size', 'card_focus', 'feature_card_image'),
            )
        }),
        ('Dates and times', {
            'fields': (
                ('publish_time', 'breaking_duration'),
                ('created', 'last_updated'),
            )
        }),
        ('Linked media', {
            'fields': (
                ('featured_image', 'featured_video', 'featured_audio'),
                ('review', 'poll'),
            )
        }),
    )

admin.site.register(models.Story, StoryAdmin)


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(models.Page, PageAdmin)
