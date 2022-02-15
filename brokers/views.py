from django.views import generic

from .models import (
    Broker,
    AccountType
    )


class BrokerListPageView(generic.ListView):
    model = Broker
    context_object_name = 'brokers'
    template_name = 'brokers/brokers.html'


class BrokerDetailPageView(generic.DetailView):
    model = Broker
    context_object_name = 'detail'
    template_name = 'brokers/detail.html'

    def get_context_data(self, *args, **kwargs):
        broker = self.object.name
        context = super(BrokerDetailPageView, self).get_context_data(*args, **kwargs)
        context['account_size'] = AccountType.objects.filter(broker__name=broker)
        return context
