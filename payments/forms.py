from django import forms
from django.forms import MultipleChoiceField, ChoiceField
from paypal.standard.forms import PayPalPaymentsForm

class CheckoutForm(forms.Form):
    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_zip = forms.CharField(required=False)


class MyPayPalPaymentsForm(PayPalPaymentsForm):
    def render(self):
        form_open  = u'''<form action="%s" method="post">''' % (self.get_endpoint())
        form_close = u'</form>'
        # format html as you need
        submit_elm = u'''<input type="submit" value="Complete payment" class="button fit">'''
        return format_html(form_open+self.as_p()+submit_elm+form_close)