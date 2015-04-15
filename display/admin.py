from django.contrib import admin

from . import models


class CardSizeAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.CardSize, CardSizeAdmin)


class StylesheetAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Stylesheet, StylesheetAdmin)


class ScriptAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Script, ScriptAdmin)


class TemplateAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Template, TemplateAdmin)
