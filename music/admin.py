from django.contrib import admin

from .models import Album

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist')
admin.site.register(Album, AlbumAdmin)

