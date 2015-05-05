from django.contrib import admin

from . import models


class SportAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Sport, SportAdmin)


class SchoolAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.School, SchoolAdmin)


class GameAdmin(admin.ModelAdmin):
    list_display = ['date', 'sport', 'home_team', 'opposing_team',
                    'home_score', 'opposing_score']


admin.site.register(models.Game, GameAdmin)
