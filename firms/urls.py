from django.urls import path

from .views import (
    FirmPageView,
    FirmDetailPageView,
    ComparisonPageView,
    ComparisonDetailPageView,
    ComparisonSearchResultView,
    FirmsGeneralRatingView,
    CashRebateFormView,
    PayoutProofView
)


urlpatterns = [
        path('compare-propfirms/', ComparisonPageView.as_view(), name='comparison'),
        path('compare-propfirms/<slug:slug>/', ComparisonDetailPageView.as_view(), name='comparison_detail'),
        path('comparison-search/', ComparisonSearchResultView.as_view(), name='comparison_search'),
        path('general-rating/', FirmsGeneralRatingView.as_view(), name='general_rating'),
        path('cash-rebate/', CashRebateFormView.as_view(), name='rebate'),
        path('payout/', PayoutProofView.as_view(), name='payout-proof'),
        path('', FirmPageView.as_view(), name='firms'),
        path('<slug:slug>/', FirmDetailPageView.as_view(), name='firm_detail')
    ]
