from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from competition.models import Competition
from brokers.models import Broker
from firms.models import (
    PropFirm,
    FirmComparison,
    FirmsGeneralRating
    )

from analytics.models import FXBlueAnalytic
from updates.models import Blog


def freq_and_prior():
    changefreq = "daily"
    priority = 0.5
    return freq_and_prior


class StaticSitemapView(Sitemap):
    freq_and_prior()

    def items(self):
        return ['about', 'privacy', 'index']

    def location(self, item):
        return reverse(item)


class PropFirmSitemapView(Sitemap):

    def items(self):
        return PropFirm.objects.all()


class FirmComparisonSitemapView(Sitemap):

    def items(self):
        return FirmComparison.objects.all()


class BlogSitemapView(Sitemap):

    def items(self):
        return Blog.objects.all()

"""
class FirmsGeneralRatingSitemapView(Sitemap):

    def items(self):
        return FirmsGeneralRating.objects.all()


class BrokerSitemapView(Sitemap):
    freq_and_prior()

    def items(self):
        return Broker.objects.all()


class AnalyticsSitemapView(Sitemap):
    freq_and_prior()

    def items(self):
        return FXBlueAnalytic.objects.all()



class CompetitionSitemapView(Sitemap):
    freq_and_prior()

    def items(self):
        return Competition.objects.all()
"""
