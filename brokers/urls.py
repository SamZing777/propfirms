from django.urls import path

from .views import (
    BrokerListPageView,
    BrokerDetailPageView
    )


urlpatterns = [
        path('', BrokerListPageView.as_view(), name='brokers'),
        path('<slug:slug>/', BrokerDetailPageView.as_view(), name='broker_detail')
    ]
