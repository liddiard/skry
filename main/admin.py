from django.contrib import admin
from main.models import Author

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Author)
