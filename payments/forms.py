from django import forms
from django.forms import MultipleChoiceField, ChoiceField
from paypal.standard.forms import PayPalPaymentsForm
from django.utils.html import format_html

class CheckoutForm(forms.Form):
    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_zip = forms.CharField(required=False)




