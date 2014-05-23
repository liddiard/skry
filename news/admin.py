from django.contrib import admin

from . import models


class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Author, AuthorAdmin)


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url_slug': ('title',)}
    readonly_fields = ('created', 'last_updated')
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
                ('category', 'position'), 
                ('tag', 'series'),
            )
        }),
        ('Card', {
            'fields': (
                ('card', 'card_size', 'card_crop', 'feature_card_image'), 
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

admin.site.register(models.Article, ArticleAdmin)


class InternalArticleCommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.InternalArticleComment, InternalArticleCommentAdmin)


class CardSizeAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.CardSize, CardSizeAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(models.Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(models.Tag, TagAdmin)


class TemplateAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Template, TemplateAdmin)


class PageAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Page, PageAdmin)


class ImageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('image', 'credit', 'caption')
        }),
    )

admin.site.register(models.Image, ImageAdmin)


class VideoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('youtube_id', 'title', 'credit', 'caption')
        }),
    )

admin.site.register(models.Video, VideoAdmin)


class AudioAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'mp3', 'ogg', 'credit', 'caption')
        }),
    )

admin.site.register(models.Audio, AudioAdmin)


class ReviewAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Review, ReviewAdmin)


class PollAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Poll, PollAdmin)


class PollChoiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.PollChoice, PollChoiceAdmin)
