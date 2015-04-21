from django.contrib import admin

from . import models


class JobInline(admin.TabularInline):
    model = models.Job

    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'organization', 'email',
                    'twitter', 'user']
    inlines = (JobInline,)


admin.site.register(models.Author, AuthorAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Organization, OrganizationAdmin)


class PositionAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Position, PositionAdmin)
