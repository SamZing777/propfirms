from django.contrib import admin

from .models import (
    User,
    TraderProfile
)


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']
    search_fields = ['username', 'email']


class TraderProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'telegram_id', 'country']


admin.site.register(User, UserAdmin)
admin.site.register(TraderProfile, TraderProfileAdmin)
