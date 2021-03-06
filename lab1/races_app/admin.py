from django.contrib import admin
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from races_app.models import Race, Horse, Participation, Organization, Bet, UserDetail


# class ParticipationInline(admin.TabularInline):
#     model = Participation
#     extra = 1
#     readonly_fields = ('place',)

class ParticipationInline(admin.TabularInline):
    model = Participation


class BetInline(admin.TabularInline):
    model = Bet


class UserDetailInline(admin.StackedInline):
    model = UserDetail
    extra = 1
    max_num = 1
    can_delete = False

    fields = ('avatar',)


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


class CustomUserAdmin(UserAdmin):
    model = User
    inlines = [
        BetInline,
        UserDetailInline
    ]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Race, RaceAdmin)
admin.site.register(Horse, HorseAdmin)
admin.site.register(Organization)
