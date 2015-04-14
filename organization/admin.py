from django.contrib import admin

from . import models


class SectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'parent', 'position']

admin.site.register(models.Section, SectionAdmin)


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(models.Tag, TagAdmin)
