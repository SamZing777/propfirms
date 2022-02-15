from django.contrib import admin

from .models import (
    Broker,
    AccountType
    )


class AccountInline(admin.StackedInline):
    model = AccountType
    extra = 1


class BrokerAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_founded', 'website']
    inlines = [AccountInline,]


admin.site.register(Broker, BrokerAdmin)
