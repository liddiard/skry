from django.contrib import admin

from ..models import display


class CardSizeAdmin(admin.ModelAdmin):
    pass

admin.site.register(display.CardSize, CardSizeAdmin)



class TemplateAdmin(admin.ModelAdmin):
    pass

admin.site.register(display.Template, TemplateAdmin)
