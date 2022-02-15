from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from django.urls import reverse
from ckeditor.fields import RichTextField
from djmoney.models.fields import MoneyField

from users.models import User


class Broker(models.Model):

    RATINGS = (
        ('Good', 'Good'),
        ('Okay', 'Okay'),
        ('Very good', 'Very good'),
        ('Poor', 'Poor')
        )

    YES_NO = (
        ('Yes', 'Yes'),
        ('No', 'No')
        )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True,
			     always_update=False, default='')
    date_founded = models.DateField()
    slogan = models.CharField(max_length=150, blank=True, null=True)
    website = models.URLField(help_text='Affiliate link')
    bonus = models.CharField(max_length=100, null=True, blank=True)
    customer_satisfaction = models.CharField(max_length=15, choices=RATINGS)
    support = models.CharField(max_length=50)
    platforms = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=200)
    payout_method = models.CharField(max_length=200)
    copy_trading = models.CharField(max_length=5, choices=YES_NO)
    leverage = models.CharField(max_length=50)
    lot_size = models.CharField(max_length=50)
    rating = models.CharField(max_length=15, choices=RATINGS)
    trust_pilot = models.URLField()
    license_and_regulators = models.CharField(max_length=255)
    minimum_deposit = MoneyField(max_digits=10, decimal_places=4, null=True,
                        blank=True, default_currency='USD',)
    note = RichTextField(verbose_name='info')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('broker_detail', args=str([self.slug]))


class AccountType(models.Model):
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    spreads = models.CharField(max_length=200)
    commission = MoneyField(max_digits=5, decimal_places=2, null=True,
                        blank=True, default_currency='USD',)
    minimum_deposit = MoneyField(max_digits=10, decimal_places=4, null=True,
                        blank=True, default_currency='USD',)

    def __str__(self):
        return self.name
