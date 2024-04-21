from django import forms
from django.core.cache import cache
from .models import CryptoAlert
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import requests


class CryptoAlertForm(forms.ModelForm):
    cryptocurrency = forms.ChoiceField(choices=[('KRAKEN_SPOT_BTC_EUR', 'KRAKEN_SPOT_BTC_EUR'),('KRAKEN_SPOT_BTC_USD', 'KRAKEN_SPOT_BTC_USD')], required=True)

    class Meta:
        model = CryptoAlert
        fields = ['cryptocurrency', 'price', 'alert_type', 'name']

    def __init__(self, *args, **kwargs):
        super(CryptoAlertForm, self).__init__(*args, **kwargs)

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label=_("Adresse email"), max_length=254)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
