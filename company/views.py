from django.views import generic


class IndexPageView(generic.TemplateView):
    template_name = 'company/index.html'


class AboutPageView(generic.TemplateView):
    template_name = 'company/about.html'


class PrivacyPolicyPageView(generic.TemplateView):
    template_name = 'company/privacy.html'


class AdsView(generic.TemplateView):
    template_name = 'company/ads.txt'


class CopyTradingPageView(generic.TemplateView):
    template_name = 'company/copy_trading.html'
