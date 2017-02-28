import reversion
from reversion.admin import VersionAdmin
from django.contrib import admin

from . import models


class PhotoRequestAdmin(VersionAdmin):
    list_display = ['story', 'location', 'time']


admin.site.register(models.PhotoRequest, PhotoRequestAdmin)


class GraphicRequestAdmin(VersionAdmin):
    list_display = ['story']


admin.site.register(models.GraphicRequest, GraphicRequestAdmin)


class IllustrationRequestAdmin(VersionAdmin):
    list_display = ['story']


admin.site.register(models.IllustrationRequest, IllustrationRequestAdmin)
