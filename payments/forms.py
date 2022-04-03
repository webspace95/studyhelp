from django import forms
from django.forms import MultipleChoiceField, ChoiceField

class CheckoutForm(forms.Form):
    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_zip = forms.CharField(required=False)

