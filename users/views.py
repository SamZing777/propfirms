from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.core.mail import send_mail
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import EmailMultiAlternatives
from django.template import Context


from .models import (
    User,
    TraderProfile
    )

from analytics.models import Performance

from .forms import (
    UserSignUpForm,
    UserProfileForm
    )



def register(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            htmly = get_template('users/signup_email.html')
            person = { 'username': username }
            subject, from_email, to = 'welcome', 'admin@propfirms.co.uk', email
            html_content = htmly.render(person)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserSignUpForm()
    return render(request, 'users/signup.html', {'form': form, 'title':'reqister here'})


class UserProfileView(generic.CreateView, LoginRequiredMixin):
    form_class = UserProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'users/profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        profile = self.request.user
        context = super(UserProfileView, self).get_context_data(*args, **kwargs)
        context['profile'] = TraderProfile.objects.filter(user=profile)
        context['performance'] = Performance.objects.filter(user=profile)
        return context
