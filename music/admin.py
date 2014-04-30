from django.contrib import admin

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist')
admin.site.register(Album, AlbumAdmin)

