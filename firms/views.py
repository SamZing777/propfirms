from django.views import generic
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.urls import reverse_lazy
from django import forms
from django.http import HttpResponse
from cloudinary.forms import cl_init_js_callbacks

from .models import (
    PropFirm,
    FundingPlan,
    ScalingPlan,
    AccountSize,
    Payout,
    FirmComparison,
    FirmsGeneralRating,
    GeneralRatingNote,
    TradersPayoutProof,
    )

from .forms import (
    CashRebateForm,
    TradersPayoutProofForm
    )


class FirmPageView(generic.ListView):
    model = PropFirm
    context_object_name = 'firms'
    template_name = 'firms/firms.html'


class FirmDetailPageView(generic.DetailView):
    model = PropFirm
    context_object_name = 'detail'
    template_name = 'firms/firm_detail.html'

    def get_context_data(self, *args, **kwargs):
        firm = self.object.name
        context = super(FirmDetailPageView, self).get_context_data(*args, **kwargs)
        context['plans'] = FundingPlan.objects.filter(firm__name=firm)
        context['scaling'] = ScalingPlan.objects.filter(firm__name=firm)
        context['payout'] = Payout.objects.filter(firm__name=firm)
        context['account_size'] = AccountSize.objects.filter(firm__name=firm)
        return context


class ComparisonPageView(generic.ListView):
    model = FirmComparison
    context_object_name = 'comparison'
    template_name = 'firms/comparison.html'


"""
    def get_context_data(self, *args, **kwargs):
        firm = self.object.firmA
        context = super(ComparisonPageView, self).get_context_data(*args, **kwargs)
        context['funding_plan'] = FundingPlan.objects.filter(firm__name=firm)
        return context
"""


class ComparisonDetailPageView(generic.DetailView):
    model = FirmComparison
    context_object_name = 'firm'
    template_name = 'firms/compare.html'

    def get_context_data(self, *args, **kwargs):
        firm = self.object.firmA
        firm_b = self.object.firmB
        context = super(ComparisonDetailPageView, self).get_context_data(*args, **kwargs)
        context['plans'] = FundingPlan.objects.filter(firm__name=firm)
        context['scaling'] = ScalingPlan.objects.filter(firm__name=firm)
        context['payout'] = Payout.objects.filter(firm__name=firm)
        context['account_size'] = AccountSize.objects.filter(firm__name=firm)

        context['firm_b_plans'] = FundingPlan.objects.filter(firm__name=firm_b)
        context['firm_b_scaling'] = ScalingPlan.objects.filter(firm__name=firm_b)
        context['firm_b_payout'] = Payout.objects.filter(firm__name=firm_b)
        context['firm_b_account_size'] = AccountSize.objects.filter(firm__name=firm_b)
        return context


class ComparisonSearchResultView(generic.ListView):
    model = PropFirm
    context_object_name = 'searches'
    template_name = 'firms/comparison_search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        queryTwo = self.request.GET.get('queryTwo')

        firm = PropFirm.objects.filter(
            Q(name__icontains=query)
        )

        firmTwo = PropFirm.objects.filter(
            Q(name__icontains=queryTwo)
        )

        combine_firm = firm | firmTwo
        return combine_firm


class FirmsGeneralRatingView(generic.ListView):
    model = FirmsGeneralRating
    context_object_name = 'rating'
    template_name = 'firms/firm_general_rating.html'

    def get_context_data(self, *args, **kwargs):
        context = super(FirmsGeneralRatingView, self).get_context_data(*args, **kwargs)
        context['rating_note'] = GeneralRatingNote.objects.all()
        return context


class CashRebateFormView(generic.CreateView):
    form_class = CashRebateForm
    success_url = reverse_lazy('profile')
    template_name = 'firms/rebate.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PayoutProofView(generic.CreateView):
    form_class = TradersPayoutProofForm
    success_url = reverse_lazy('payout-proof')
    template_name = 'firms/payout_proof.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(PayoutProofView, self).get_context_data(*args, **kwargs)
        context['payout'] = TradersPayoutProof.objects.all()
        return context
