import reversion
from django.contrib import admin

from . import models


class PhotoRequestAdmin(reversion.VersionAdmin):
    list_display = ['story', 'location', 'time']


admin.site.register(models.PhotoRequest, PhotoRequestAdmin)


class GraphicRequestAdmin(reversion.VersionAdmin):
    list_display = ['story']


admin.site.register(models.GraphicRequest, GraphicRequestAdmin)


class IllustrationRequestAdmin(reversion.VersionAdmin):
    list_display = ['story']


admin.site.register(models.IllustrationRequest, IllustrationRequestAdmin)
