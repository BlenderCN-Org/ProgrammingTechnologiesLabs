from django.contrib import admin

# Register your models here.
from races_app.models import Race, Horse, Participation, Organization


# class ParticipationInline(admin.TabularInline):
#     model = Participation
#     extra = 1
#     readonly_fields = ('place',)

class ParticipationInline(admin.TabularInline):
    model = Participation


class RaceAdmin(admin.ModelAdmin):
    model = Race
    inlines = [
        ParticipationInline,
    ]
    # filter_horizontal = ('participants',)
    list_display = ['track', 'loops', 'date']


class HorseAdmin(admin.ModelAdmin):
    model = Horse
    inlines = [
        ParticipationInline,
    ]
    list_display = ['name']


admin.site.register(Race, RaceAdmin)
admin.site.register(Horse, HorseAdmin)
admin.site.register(Organization)
