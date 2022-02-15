from django.urls import path

from .views import (
    register,
    UserProfileView
    )


urlpatterns = [
        path('signup/', register, name='signup'),
        path('profile/', UserProfileView.as_view(), name='profile'),
    ]
