from django.contrib import admin

from . import models


class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Author, AuthorAdmin)


class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Article, ArticleAdmin)


class InternalArticleCommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.InternalArticleComment, InternalArticleCommentAdmin)


class CardSizeAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.CardSize, CardSizeAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Tag, TagAdmin)


class TemplateAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Template, TemplateAdmin)


class PageAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Page, PageAdmin)


class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Image, ImageAdmin)


class VideoAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Video, VideoAdmin)


class AudioAdmin(admin.ModelAdmin):
    pass

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
