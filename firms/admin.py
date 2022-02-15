from django.contrib import admin

from .models import (
    FundingPlan,
    Payout,
    ScalingPlan,
    PropFirm,
    AccountSize,
    FirmComparison,
    CashRebate,
    FirmsGeneralRating,
    GeneralRatingNote,
    TradersPayoutProof
)

"""
class FundingPlanAdmin(admin.ModelAdmin):
    list_display = ['firm', 'name']


class ScalingPlanAdmin(admin.ModelAdmin):
    list_display = ['firm', 'package']


class PayoutAdmin(admin.ModelAdmin):
    list_display = ['firm', 'package', 'profit_split', 'interval']
"""


class AccountInlines(admin.StackedInline):
    model = AccountSize
    extra = 1


class FundingInlines(admin.TabularInline):
    model = FundingPlan
    extra = 1


class PayoutInlines(admin.StackedInline):
    model = Payout
    extra = 1


class ScalingInlines(admin.StackedInline):
    model = ScalingPlan
    extra = 1


class FirmAdmin(admin.ModelAdmin):
    list_display = ['name', 'CEO', 'website', 'overall_rating']
    inlines = [FundingInlines, AccountInlines, PayoutInlines, ScalingInlines,]


class CashRebateAdmin(admin.ModelAdmin):
    list_display = ['user', 'propfirm', 'date_purchased', 'expects']


class FirmComparisonAdmin(admin.ModelAdmin):
    list_display = ['firmA', 'firmB', 'date_updated']


class FirmsGeneralRatingAdmin(admin.ModelAdmin):
    list_display = ['firm', 'established_year', 'total_score']


class GeneralRatingNoteAdmin(admin.ModelAdmin):
    list_display = ['abstract', 'date_updated']


class TradersPayoutProofAdmin(admin.ModelAdmin):
    list_display = ['user', 'firm', 'payout']


admin.site.register(PropFirm, FirmAdmin)
admin.site.register(CashRebate, CashRebateAdmin)
admin.site.register(FirmComparison, FirmComparisonAdmin)
admin.site.register(FirmsGeneralRating, FirmsGeneralRatingAdmin)
admin.site.register(GeneralRatingNote, GeneralRatingNoteAdmin)
admin.site.register(TradersPayoutProof, TradersPayoutProofAdmin)
