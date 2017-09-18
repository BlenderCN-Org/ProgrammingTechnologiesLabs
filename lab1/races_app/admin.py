from django.contrib import admin

# Register your models here.
from races_app.models import Race, Horse, Participation


class ParticipationInline(admin.TabularInline):
    model = Participation


class RaceAdmin(admin.ModelAdmin):
    model = Race
    inlines = [
        ParticipationInline,
    ]
    filter_horizontal = ('horses',)
    list_display = ['track', 'loops', 'date']


class HorseAdmin(admin.ModelAdmin):
    model = Horse
    inlines = [
        ParticipationInline,
    ]
    list_display = ['name']


admin.site.register(Race, RaceAdmin)
admin.site.register(Horse, HorseAdmin)
