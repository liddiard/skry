from django.contrib import admin
from prime.models import Issue, Article, Image

class IssueAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date')
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Issue, IssueAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'issue')
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Article, ArticleAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'caption', 'author', 'issue')
    readonly_fields = ('id',)
admin.site.register(Image, ImageAdmin)
