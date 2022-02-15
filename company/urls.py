from django.urls import path

from .views import (
    IndexPageView,
    AboutPageView,
    PrivacyPolicyPageView,
    AdsView,
    CopyTradingPageView
    )


urlpatterns = [
        path('', IndexPageView.as_view(), name='index'),
        path('about/', AboutPageView.as_view(), name='about'),
        path('privacy/', PrivacyPolicyPageView.as_view(), name='privacy'),
        path('copy-trading/', CopyTradingPageView.as_view(), name='copy-trading'),
        path('ads/', AdsView.as_view(), name='ads')
    ]
