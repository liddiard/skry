from django.contrib import admin

from . import models


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(models.Post, PostAdmin)


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(models.Project, ProjectAdmin)


class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Image, ImageAdmin)
