from django.urls import path

from .views import (
    TradingViewPage,
    CurrencyConverterPageView,
    PipCalculatorPageView,
    ProfitCalculatorPageView,
    CompoundingCalculatorPageView,
    AnalyticsPageView,
    CreateAnalyticView,
    CreateFavouriteInstrumentView
    )



urlpatterns = [
        path('analyse/', TradingViewPage.as_view(), name='tradingview'),
        path('currency-converter/', CurrencyConverterPageView.as_view(), name='currency-converter'),
        path('pip-calculator/', PipCalculatorPageView.as_view(), name='pip-calculator'),
        path('profit-calculator/', ProfitCalculatorPageView.as_view(), name='profit-calculator'),
        path('compound-calculator/', CompoundingCalculatorPageView.as_view(), name='compound-calculator'),
        path('', AnalyticsPageView.as_view(), name='analytics'),
        path('create/', CreateAnalyticView.as_view(), name='create-analytic'),
        path('create-instrument/', CreateFavouriteInstrumentView.as_view(), name='create-instrument')
    ]
