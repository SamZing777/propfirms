from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap


from .sitemap import (
    StaticSitemapView,
    PropFirmSitemapView,
    FirmComparisonSitemapView,
    BlogSitemapView
    )

"""
BrokerSitemapView,
CompetitionSitemapView,
AnalyticsSitemapView,
 FirmsGeneralRatingSitemapView

"""

sitemaps = {
    'static': StaticSitemapView,
    'propfirms': PropFirmSitemapView,
    'comparison': FirmComparisonSitemapView,
    'blog': BlogSitemapView
    }

"""
'broker': BrokerSitemapView,
'competition': CompetitionSitemapView,
'analytics': AnalyticsSitemapView,
'rating': FirmsGeneralRatingSitemapView
"""


urlpatterns = [
    path('', include('company.urls')),
    path('propfirms/', include('firms.urls')),
    path('user/', include('users.urls')),
    path('competition/', include('competition.urls')),
    path('analytics/', include('analytics.urls')),
    path('blog/', include('updates.urls')),
    path('brokers/', include('brokers.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('staff/', include('staffs.urls')),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps},
	                     name='django.contrib.sitemaps.views.sitemap'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
]


admin.site.site_header = "Prop Firms Admin"
admin.site.site_title = "Prop Firms Admin"
admin.site.index_title = "Prop Firms Admin"
