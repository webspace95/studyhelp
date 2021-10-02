from django import forms
from django.forms import MultipleChoiceField, ChoiceField

SUBJECT_CHOICES =(
    ("1", "Accounting and Finance"),
    ("2", "Arts and Humanities"),
    ("3", "Economics"),
    ("4", "Engineering"),
    ("5", "IT Computer Science"),
    ("6", "Law"),
    ("7", "Management"),
    ("8", "Meddical Sciences"),
    ("9", "Science and Maths"),
    ("10", "Statistics"),
    ("11", "Other Subjects"),
)

class ContactForm(forms.Form):
    name = forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'name':'name','id':'name'}))
    email = forms.EmailField( label='',max_length=100 ,widget=forms.EmailInput(attrs={'name':'email','id':'email'}))
    message = forms.CharField( label='',widget=forms.Textarea(attrs={'id':'message','name':'message','rows':5}))

class OrderForm(forms.Form):
    pass
    name = forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'name':'name','id':'name'}))
    email = forms.EmailField( label='',max_length=100 ,widget=forms.EmailInput(attrs={'name':'email','id':'email'}))
    title = forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'name':'title','id':'title'}))
    pages = forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'name':'pages','id':'pages'}))
    deadline = forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'name':'deadline','id':'pages'}))
    type = forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'name':'type','id':'type'}))
    format = forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'name':'format','id':'format'}))
    subject = forms.MultipleChoiceField(label='',widget=forms.SelectMultiple(attrs={'name':'subject','id':'subject'}),choices=SUBJECT_CHOICES,)
    academiclevel = forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'name':'academiclevel','id':'academiclevel'}))
    instructions = forms.CharField( label='',widget=forms.Textarea(attrs={'id':'message','name':'message','rows':5}))
    #name
    #email
    #instructions
    #title
    #no of pages
    #type of paper
    #paper format
    #subject
    #education level
    #file field

