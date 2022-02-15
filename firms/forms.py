from django import forms
from cloudinary.forms import CloudinaryJsFileField
from ckeditor.widgets import CKEditorWidget

from .models import (
    CashRebate,
    TradersPayoutProof
    )


class DateInput(forms.DateInput):
    input_type = 'date'


class CashRebateForm(forms.ModelForm):
    picture = CloudinaryJsFileField
    date_purchased = forms.DateField(widget=DateInput)

    class Meta:
        model = CashRebate
        fields = ['propfirm', 'picture', 'order_number', 'comment', 'expects', 'date_purchased']

    def save(self, user=None):
        rebate = super(CashRebateForm, self).save(commit=False)
        if user:
            rebate.user = user
        rebate.save()
        return rebate


class TradersPayoutProofForm(forms.ModelForm):
    attachment = CloudinaryJsFileField

    class Meta:
        model = TradersPayoutProof
        fields = ['firm', 'package', 'attachment', 'account_size', 'payout',
                    'additional_remark']

    def save(self, user=None):
        proof = super(TradersPayoutProofForm, self).save(commit=False)
        if user:
            proof.user = user
        proof.save()
        return proof

