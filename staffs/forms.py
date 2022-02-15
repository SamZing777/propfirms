from django import forms
from cloudinary.forms import CloudinaryJsFileField
from ckeditor.widgets import CKEditorWidget

from firms.models import (
    PropFirm,
    FundingPlan,
    AccountSize,
    ScalingPlan,
    Payout,
    FirmComparison
    )


class DateInput(forms.DateInput):
    input_type = 'date'


class AddPropFirmForm(forms.ModelForm):
    note = forms.CharField(widget=CKEditorWidget())
    date_founded = forms.DateField(widget=DateInput)

    class Meta:
        model = PropFirm
        fields = [
        'name', 'date_founded', 'CEO', 'motto', 'website', 'discount_code',
        'cash_back', 'customer_satisfaction', 'automation', 'communication',
        'leadership', 'adaptability', 'ethics', 'good_will', 'conflict_resolution_ability',
        'innovation', 'face_criticism', 'support', 'platforms', 'payment_method',
        'payout_method', 'consistency', 'trade_copier', 'EAs', 'account_metrix',
        'trial', 'broker_or_server', 'overall_rating', 'note'
    ]

    def save(self, user=None):
        staff = super(AddPropFirmForm, self).save(commit=False)
        if user:
            staff.user = user
        staff.save()
        return staff


class AddFundingPlanForm(forms.ModelForm):

    class Meta:
        model = FundingPlan
        fields = [
        'firm', 'name', 'profit_target', 'profit_split', 'daily_dd', 'max_dd',
        'leverage', 'instruments', 'consistency', 'fee_refund',
        'maximum_funded_account', 'maximum_account_size', 'minimum_duration',
        'maximum_duration',
    ]

    def save(self, user=None):
        staff = super(AddFundingPlanForm, self).save(commit=False)
        if user:
            staff.user = user
        staff.save()
        return staff


class AddAccountSizeForm(forms.ModelForm):

    class Meta:
        model = AccountSize
        fields = [
        'firm', 'plan', 'size', 'price'
    ]


class AddPayoutForm(forms.ModelForm):

    class Meta:
        model = Payout
        fields = [
        'firm', 'package', 'profit_split', 'interval'
    ]


class AddScalingPlanForm(forms.ModelForm):

    class Meta:
        model = ScalingPlan
        fields = [
        'firm', 'package', 'condition', 'scale_by', 'max_equity'
    ]


class AddFirmComparisonForm(forms.ModelForm):

    class Meta:
        model = FirmComparison
        fields = [
        'firmA', 'firmB', 'firm_a_rules', 'firm_b_rules', 'comment', 'date_updated'
    ]

    def save(self, user=None):
            staff = super(AddFirmComparisonForm, self).save(commit=False)
            if user:
                staff.user = user
            staff.save()
            return staff

