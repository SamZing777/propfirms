from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField



class User(AbstractUser):
    pass

    def __str__(self):
        return self.username


class TraderProfile(models.Model):
    TRADING_STYLE = (
        ('HFT', 'HFT'),
        ('Intraday', 'Intraday'),
        ('Position', 'Position'),
        ('Scalp', 'Scalp'),
        ('Swing', 'Swing'),
        ('Scalp and swing', 'Scalp and swing'),
        ('Intraday and scalp', 'Intraday and scalp'),
        ('Intraday and swing', 'Intraday and swing'),
        ('Intraday, scalp and swing', 'Intraday, scalp and swing'),
        ('All', 'All')
    )

    YES_NO = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Rather not say', 'Rather not say')
    )

    RISK = (
        ('Aggressive', 'Aggressive'),
        ('Low risk', 'Low risk'),
        ('Normal', 'Normal'),
        ('Rather not say', 'Rather not say')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)
    profile_link = models.URLField(help_text='Profile Link from Trading View',
                    null=True, blank=True)
    picture = CloudinaryField('image', null=True, blank=True, folder='profile')
    country = CountryField(blank_label='(select country)')
    phone_number = PhoneNumberField(null=True, blank=True,
                    help_text='International format, e.g: +44, +91, +234, etc..')
    telegram_id = models.CharField(max_length=100, null=True, blank=True)
    trading_strategy = models.CharField(max_length=150)
    style = models.CharField(max_length=30, choices=TRADING_STYLE)
    trading_with_firms = models.CharField(max_length=20, choices=YES_NO)
    risk_appetite = models.CharField(max_length=20, choices=RISK)
    years_of_experience = models.CharField(max_length=2)

    def __str__(self):
        return str(self.user)
