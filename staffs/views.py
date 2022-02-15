import csv
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse

from users.models import User
from competition.models import CompetitionApplication
from updates.models import Blog

from .forms import (
        AddPropFirmForm,
        AddFundingPlanForm,
        AddAccountSizeForm,
        AddScalingPlanForm,
        AddPayoutForm,
        AddFirmComparisonForm
    )


def exportCSV(request):
    traders = User.objects.all()
    response = HttpResponse('text/csv')
    response['content-Disposition'] = 'attachment; filename=users_tuesday.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'First name', 'Last name', 'Email'])
    trader = traders.values_list('id', 'first_name', 'last_name', 'email')

    for user in trader:
        writer.writerow(user)
    return response


def exportCompetitionApplication(request):
    competitors = CompetitionApplication.objects.all()
    response = HttpResponse('text/csv')
    response['content-Disposition'] = 'attachment; filename=propfirms_competitors_list.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Username', 'Competition', 'Server', 'Platform', 'Login', 'Investor password'])
    competition = competitors.values_list('id', 'user', 'name', 'server', 'platform', 'account_number', 'investor_password')

    for trader in competition:
        writer.writerow(trader)
    return response


class StaffDashboardView(generic.TemplateView):
    template_name = 'staffs/staff.html'


class UserListView(generic.ListView):
    model = User
    context_object_name = 'users'
    paginate_by = 40
    template_name = 'staffs/users.html'


class CompetitionPageListView(generic.ListView):
    model = CompetitionApplication
    context_object_name = 'application'
    paginate_by = 40
    template_name = 'staffs/competition.html'


class PropFirmCreateView(generic.CreateView):
    form_class = AddPropFirmForm
    success_url = reverse_lazy('firms')
    template_name = 'staffs/add_propfirm.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PropFirmUpdateView(generic.UpdateView):
    form_class = AddPropFirmForm
    success_url = reverse_lazy('firms')
    template_name = 'staffs/update_propfirm.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FundingPlanCreateView(generic.CreateView):
    form_class = AddFundingPlanForm
    success_url = reverse_lazy('add-funding')
    template_name = 'staffs/add_funding.html'


class FundingPlanUpdateView(generic.UpdateView):
    form_class = AddFundingPlanForm
    success_url = reverse_lazy('firms')
    template_name = 'staffs/update_funding.html'


class AccountSizeCreateView(generic.CreateView):
    form_class = AddAccountSizeForm
    success_url = reverse_lazy('add-account-size')
    template_name = 'staffs/add_account_size.html'


class AccountSizeUpdateView(generic.CreateView):
    form_class = AddAccountSizeForm
    success_url = reverse_lazy('firms')
    template_name = 'staffs/update_account_size.html'


class ScalingPlanCreateView(generic.CreateView):
    form_class = AddScalingPlanForm
    success_url = reverse_lazy('add-scaling')
    template_name = 'staffs/add_scaling.html'


class ScalingPlanUpdateView(generic.UpdateView):
    form_class = AddScalingPlanForm
    success_url = reverse_lazy('firms')
    template_name = 'staffs/update_scaling.html'


class PayoutCreateView(generic.CreateView):
    form_class = AddPayoutForm
    success_url = reverse_lazy('add-payout')
    template_name = 'staffs/add_payout.html'


class PayoutUpdateView(generic.UpdateView):
    form_class = AddPayoutForm
    success_url = reverse_lazy('firms')
    template_name = 'staffs/update_payout.html'


class FirmComparisonCreateView(generic.CreateView):
    form_class = AddFirmComparisonForm
    success_url = reverse_lazy('add-comparison')
    template_name = 'staffs/add_firm_comparison.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FirmComparisonUpdateView(generic.UpdateView):
    form_class = AddFirmComparisonForm
    success_url = reverse_lazy('firms')
    template_name = 'staffs/update_comparison.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MyPostPageView(generic.ListView):
    model = Blog
    paginate_by = 12
    template_name = 'staffs/my_posts.html'

    def get_context_data(self, *args, **kwargs):
        staff = self.request.user
        context = super(MyPostPageView, self).get_context_data(*args, **kwargs)
        context['posts'] = Blog.objects.filter(user=staff)
        return context
