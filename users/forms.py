from django.contrib.auth.forms import UserCreationForm
from django import forms
from cloudinary.forms import CloudinaryJsFileField

from .models import (
    User,
    TraderProfile
    )


class UserSignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']



class UserProfileForm(forms.ModelForm):
    picture = CloudinaryJsFileField

    class Meta:
        model = TraderProfile
        fields = ['profile_link', 'picture', 'country', 'phone_number', 'bio', 'telegram_id', 'years_of_experience',
                'trading_with_firms', 'style', 'trading_strategy']

        def save(self, user=None):
            profile = super(UserProfileForm, self).save(commit=False)
            if user:
                profile.user = user
            profile.save()
            return profile
