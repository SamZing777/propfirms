from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from autoslug import AutoSlugField
from djmoney.models.fields import MoneyField

from competition.models import Competition

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from='name', unique=True,
			     always_update=False, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Instrument(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    tag = models.CharField(max_length=20, help_text='Eg: Majors, Minors...',
                            null=True, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True,
			     always_update=False, default='')
    symbol = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class FavouriteInstrument(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='instrument', unique=True,
			     always_update=False, default='')

    def __str__(self):
        return str(self.user)


class FXBlueAnalytic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='user', unique=True,
			     always_update=False, default='')
    link = models.URLField(help_text='E.g: https://www.fxblue.com/users/oceanman')

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
	    return reverse('analytics', args=[str(self.slug)])

    class Meta:
	    ordering = ['user']


class Performance(models.Model):

    PERFORMANCE = (
        ('Good', 'Good'),
        ('Average', 'Average'),
        ('Very Good', 'Very Good'),
        ('Poor', 'Poor')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='user', unique=True,
			     always_update=False, default='')
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    total_trades = models.PositiveIntegerField()
    total_pip = models.SmallIntegerField()
    pip_volume = models.SmallIntegerField()
    profit_and_loss = models.IntegerField()
    p_and_l_volume = models.SmallIntegerField()
    starting_equity = MoneyField(max_digits=40, decimal_places=2,
                        default_currency='USD')
    closing_balance = MoneyField(max_digits=40, decimal_places=2,
                        default=50000, default_currency='USD')
    risk_reward = models.DecimalField(max_digits=5, decimal_places=2)
    rr_volume = models.SmallIntegerField()
    profit_factor = models.DecimalField(max_digits=5, decimal_places=2)
    profit_factor_volume = models.SmallIntegerField()
    position = models.CharField(max_length=20)
    behaviour = models.CharField(max_length=20, choices=PERFORMANCE)
    behaviour_volume = models.SmallIntegerField()
    ability = models.CharField(max_length=20, choices=PERFORMANCE)
    ability_volume = models.SmallIntegerField()

    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ['user']
