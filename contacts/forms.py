from  django import forms
from .models import Contact


class ContactForm (forms.Form): 
    name = forms.CharField(max_length=100,widget= forms.TextInput(attrs={'id':'name'}))
    email = forms.EmailField(max_length=254, widget= forms.EmailInput(attrs={'id':'email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'id':'message'}))