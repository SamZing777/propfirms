from django.views import generic
from django.urls import reverse_lazy


from .models import (
        Category,
        Instrument,
        FavouriteInstrument,
        FXBlueAnalytic
    )

from .forms import (
    CreateAnalyticsForm,
    FavouriteInstrumentForm
    )


class TradingViewPage(generic.TemplateView):
    template_name = 'analytics/tradingview.html'


class CurrencyConverterPageView(generic.TemplateView):
    template_name = 'analytics/calculator.html'


class PipCalculatorPageView(generic.TemplateView):
    template_name = 'analytics/pip_calculator.html'


class ProfitCalculatorPageView(generic.TemplateView):
    template_name = 'analytics/profit_calculator.html'


class CompoundingCalculatorPageView(generic.TemplateView):
    template_name = 'analytics/compounding_calculator.html'


class CreateAnalyticView(generic.CreateView):
    form_class = CreateAnalyticsForm
    success_url = reverse_lazy('analytics')
    template_name = 'analytics/create_analytics.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CreateFavouriteInstrumentView(generic.CreateView):
    form_class = FavouriteInstrumentForm
    success_url = reverse_lazy('analytics')
    template_name = 'analytics/create_instrument.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AnalyticsPageView(generic.ListView):
    model = FXBlueAnalytic
    template_name = 'analytics/analytics.html'

    def get_context_data(self, *args, **kwargs):
        trader = self.request.user
        context = super(AnalyticsPageView, self).get_context_data(*args, **kwargs)
        context['analytics'] = FXBlueAnalytic.objects.filter(user=trader)
        context['instruments'] = FavouriteInstrument.objects.filter(user=trader)
        return context
