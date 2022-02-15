from django.urls import path

from .views import (
        BlogPostView,
        BlogListPageView,
        BlogDetailPageView
    )


urlpatterns = [
        path('add-post/', BlogPostView.as_view(), name='add-post'),
        path('', BlogListPageView.as_view(), name='blog'),
        path('<slug:slug>/', BlogDetailPageView.as_view(), name='blog_detail')
    ]
