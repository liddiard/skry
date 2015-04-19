from django.contrib import admin

from . import models


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'organization', 'email',
                    'twitter', 'user']

admin.site.register(models.Author, AuthorAdmin)
