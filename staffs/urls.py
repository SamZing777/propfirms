from django.urls import path

from .views import (
    StaffDashboardView,
    UserListView,
    CompetitionPageListView,
    exportCSV,
    exportCompetitionApplication,
    PropFirmCreateView,
    PropFirmUpdateView,
    FundingPlanCreateView,
    FundingPlanUpdateView,
    AccountSizeCreateView,
    AccountSizeUpdateView,
    ScalingPlanCreateView,
    ScalingPlanUpdateView,
    PayoutCreateView,
    PayoutUpdateView,
    FirmComparisonCreateView,
    FirmComparisonUpdateView,
    MyPostPageView
    )


urlpatterns = [
        path('', StaffDashboardView.as_view(), name='staff'),
        path('users/', UserListView.as_view(), name='users'),
        path('competition/', CompetitionPageListView.as_view(), name='contestants'),
        path('user-csv', exportCSV, name='export-users'),
        path('competition-csv/', exportCompetitionApplication, name='export-competition'),
        path('add-firm/', PropFirmCreateView.as_view(), name='add-firm'),
        path('add-funding/', FundingPlanCreateView.as_view(), name='add-funding'),
        path('add-account-size/', AccountSizeCreateView.as_view(), name='add-account-size'),
        path('add-scaling/', ScalingPlanCreateView.as_view(), name='add-scaling'),
        path('add-payout/', PayoutCreateView.as_view(), name='add-payout'),
        path('add-comparison/', FirmComparisonCreateView.as_view(), name='add-comparison'),
        path('my-posts/', MyPostPageView.as_view(), name='my-posts')
    ]
