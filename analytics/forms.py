from django import forms

from .models import (
    FXBlueAnalytic,
    FavouriteInstrument
    )


class CreateAnalyticsForm(forms.ModelForm):

    class Meta:
        model = FXBlueAnalytic
        fields = ['link']

    def save(self, user=None):
            trader = super(CreateAnalyticsForm, self).save(commit=False)
            if user:
                trader.user = user
            trader.save()
            return trader


class FavouriteInstrumentForm(forms.ModelForm):

    class Meta:
        model = FavouriteInstrument
        fields = ['instrument']

    def save(self, user=None):
            trader = super(FavouriteInstrumentForm, self).save(commit=False)
            if user:
                trader.user = user
            trader.save()
            return trader
