from django.contrib import admin

from . import models


class CardSizeAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.CardSize, CardSizeAdmin)



class TemplateAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Template, TemplateAdmin)
