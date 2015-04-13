from django.contrib import admin

from ..models import organization


class SectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'parent', 'position']

admin.site.register(organization.Section, SectionAdmin)


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(organization.Tag, TagAdmin)
