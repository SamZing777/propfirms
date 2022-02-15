from django.contrib import admin

from .models import (
    Category,
    Instrument,
    FavouriteInstrument,
    FXBlueAnalytic,
    Performance
    )


class InstrumentInline(admin.StackedInline):
    model = Instrument
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [InstrumentInline,]


class PerformanceAdmin(admin.ModelAdmin):
    list_display = ['user', 'competition', 'total_trades', 'position', 'ability']

"""
class FavouriteInstrumentAdmin(admin.StackedInline):
    list_display = ['user', 'instrument']
"""

admin.site.register(Category, CategoryAdmin)
admin.site.register(FavouriteInstrument)
admin.site.register(FXBlueAnalytic)
admin.site.register(Performance, PerformanceAdmin)
