from django.contrib import admin

from . import models


class PhotoRequestAdmin(admin.ModelAdmin):
    list_display = ['story', 'location', 'time']


admin.site.register(models.PhotoRequest, PhotoRequestAdmin)


class GraphicRequestAdmin(admin.ModelAdmin):
    list_display = ['story']


admin.site.register(models.GraphicRequest, GraphicRequestAdmin)


class IllustrationRequestAdmin(admin.ModelAdmin):
    list_display = ['story']


admin.site.register(models.IllustrationRequest, IllustrationRequestAdmin)
