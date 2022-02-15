from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField
from djmoney.models.fields import MoneyField
from django.core.validators import MinValueValidator, MaxValueValidator

from users.models import User


class PropFirm(models.Model):

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
    CEO = models.CharField(max_length=100)
    motto = models.CharField(max_length=150, blank=True, null=True)
    website = models.URLField(help_text='Affiliate link')
    discount_code = models.CharField(max_length=20, null=True, blank=True)
    cash_back = models.CharField(max_length=40, null=True, blank=True)
    customer_satisfaction = models.CharField(max_length=15, choices=RATINGS)
    automation = models.CharField(max_length=15, choices=RATINGS)
    leadership = models.CharField(max_length=15, choices=RATINGS)
    communication = models.CharField(max_length=15, choices=RATINGS)
    ethics = models.CharField(max_length=15, choices=RATINGS)
    good_will = models.CharField(max_length=15, choices=RATINGS)
    conflict_resolution_ability = models.CharField(max_length=15,
                                    choices=RATINGS)
    innovation = models.CharField(max_length=15, choices=RATINGS)
    face_criticism = models.CharField(max_length=15, choices=RATINGS)
    adaptability = models.CharField(max_length=15, choices=RATINGS)
    support = models.CharField(max_length=15, choices=RATINGS)
    platforms = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=200)
    payout_method = models.CharField(max_length=200)
    consistency = models.CharField(max_length=5, choices=YES_NO)
    trade_copier = models.CharField(max_length=5, choices=YES_NO)
    EAs = models.CharField(max_length=5, choices=YES_NO)
    account_metrix = models.CharField(max_length=5, choices=YES_NO)
    trial = models.CharField(max_length=5, choices=YES_NO)
    broker_or_server = models.CharField(max_length=200)
    overall_rating = models.CharField(max_length=15, choices=RATINGS)
    note = RichTextField(verbose_name='info')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
	    return reverse('firm_detail', args=[str(self.slug)])

    class Meta:
	    ordering = ['name']


class FundingPlan(models.Model):
    YES_NO = (
        ('Yes', 'Yes'),
        ('No', 'No')
        )

    firm = models.ForeignKey(PropFirm, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True,
			     always_update=False, default='')
    profit_target = models.CharField(max_length=100)
    profit_split = models.CharField(max_length=50)
    daily_dd = models.CharField(max_length=50)
    max_dd = models.CharField(max_length=50)
    leverage = models.CharField(max_length=50)
    instruments = models.CharField(max_length=150)
    consistency = models.CharField(max_length=5, choices=YES_NO)
    fee_refund = models.CharField(max_length=5, choices=YES_NO)
    maximum_funded_account = models.IntegerField(null=True, blank=True)
    maximum_account_size = MoneyField(max_digits=10, decimal_places=2,
                            default_currency='USD')
    minimum_duration = models.CharField(max_length=50)
    maximum_duration = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AccountSize(models.Model):
    firm = models.ForeignKey(PropFirm, on_delete=models.CASCADE)
    plan = models.ForeignKey(FundingPlan, on_delete=models.CASCADE)
    size = MoneyField(max_digits=10, decimal_places=2,
                            default_currency='USD')
    price = MoneyField(max_digits=6, decimal_places=2,
                            default_currency='USD')
    slug = AutoSlugField(populate_from='size', unique=True,
			     always_update=False, default='')

    def __str__(self):
        return str(self.size)


class Payout(models.Model):
    firm = models.ForeignKey(PropFirm, on_delete=models.CASCADE)
    package = models.ForeignKey(FundingPlan, on_delete=models.CASCADE)
    profit_split = models.CharField(max_length=50)
    interval = models.CharField(max_length=50)

    def __str__(self):
        return str(self.package)


class ScalingPlan(models.Model):
    firm = models.ForeignKey(PropFirm, on_delete=models.CASCADE)
    package = models.ForeignKey(FundingPlan, on_delete=models.CASCADE)
    condition = models.CharField(max_length=150)
    scale_by = models.CharField(max_length=100)
    max_equity = MoneyField(max_digits=10, decimal_places=2,
                            default_currency='USD')

    def __str__(self):
        return str(self.package)


class CashRebate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    propfirm = models.ForeignKey(PropFirm, on_delete=models.CASCADE,)
    picture = CloudinaryField('auto', folder='prop_payment_proof')
    order_number = models.CharField(help_text='Could be invoice number',
                    max_length=20)
    comment = models.CharField(max_length=100, null=True, blank=True,
                help_text='you may include Funding plan, account size and paid'
                ' price')
    expects = MoneyField(max_digits=6, decimal_places=2,
                            default_currency='USD')
    date_purchased = models.DateField()

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
	    return reverse('rebate', args=[str(self.slug)])

    class Meta:
	    ordering = ['user']


class FirmComparison(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firmA = models.ForeignKey(PropFirm, on_delete=models.CASCADE,
                                related_name='firm_A')
    firmB = models.ForeignKey(PropFirm, on_delete=models.CASCADE,
                                related_name='firm_B')
    slug = AutoSlugField(populate_from='firmA', unique=True,
			     always_update=False)
    firm_a_rules = models.SmallIntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)], default=4)
    firm_b_rules = models.SmallIntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)], default=4)
    comment = models.CharField(max_length=200, null=True, blank=True)
    date_updated = models.DateField()

    def __str__(self):
        return str(self.firmA)

    def get_absolute_url(self):
	    return reverse('comparison_detail', args=[str(self.slug)])

    class Meta:
	    ordering = ['firmA']


class FirmsGeneralRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firm = models.OneToOneField(PropFirm, on_delete=models.CASCADE)
    name = models.CharField(max_length=10, default='FTMO',
                    help_text='Not more than 10 characters.')
    slug = AutoSlugField(populate_from='firm', unique=True,
			     always_update=False)
    automation = models.SmallIntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    adaptation = models.SmallIntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    communication = models.SmallIntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    conflict_resolution_ability = models.SmallIntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    CSR = models.SmallIntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    customer_satisfaction = models.SmallIntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    empathy = models.SmallIntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    ethics = models.SmallIntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    face_criticism = models.SmallIntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    good_will = models.SmallIntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    innovation = models.SmallIntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    leadership = models.SmallIntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    operation = models.SmallIntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    payout = models.SmallIntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    price = models.SmallIntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    process = models.SmallIntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    profit_split = models.SmallIntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    realism = models.SmallIntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    scaling_plan = models.SmallIntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    trading_rules = models.SmallIntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
    total_score = models.SmallIntegerField(validators=[MinValueValidator(1)],
                                            null=True, blank=True)
    established_year = models.CharField(max_length=20)

    def __str__(self):
        return str(self.firm)

    def save(self, *args, **kwargs):
        self.total_score = self.adaptation + self.automation + self.communication + self.conflict_resolution_ability + self.CSR + self.customer_satisfaction + self.empathy + self.ethics + self.face_criticism + self.good_will + self.innovation + self.leadership + self.operation + self.payout + self.price + self.process + self.profit_split + self.realism + self.scaling_plan + self.trading_rules
        super(FirmsGeneralRating, self).save(*args, **kwargs)

    def get_absolute_url(self):
	    return reverse('general_rating', args=[str(self.slug)])

    class Meta:
        ordering = ['firm']


class GeneralRatingNote(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    abstract = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='abstract', unique=True,
			     always_update=False)
    note = RichTextField(verbose_name='info')
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.abstract

    class Meta:
        ordering = ['date_updated']


class TradersPayoutProof(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firm = models.ForeignKey(PropFirm, on_delete=models.CASCADE)
    package = models.ForeignKey(FundingPlan, on_delete=models.CASCADE)
    account_size = models.ForeignKey(AccountSize, on_delete=models.CASCADE)
    payout = MoneyField(max_digits=10, decimal_places=2,
                            default_currency='USD')
    attachment = CloudinaryField('auto', folder='payout_proof')
    additional_remark = models.CharField(max_length=200, null=True, blank=True)
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ['user']
