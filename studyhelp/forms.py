from django import forms
from django.forms import MultipleChoiceField, ChoiceField

SUBJECT_CHOICES =(
    ("1","Select Subject"),
    ("2", "Accounting and Finance"),
    ("3", "Arts and Humanities"),
    ("4", "Economics"),
    ("5", "Engineering"),
    ("6", "IT Computer Science"),
    ("7", "Law"),
    ("8", "Management"),
    ("9", "Meddical Sciences"),
    ("10", "Science and Maths"),
    ("11", "Statistics"),
    ("12", "Other Subjects"),
)

ACADEMIC_LEVEL_CHOICES = (
    ("1","Select Academic Level"),
    ("2","Highschool"),
    ("3","College"),
    ("4","University"),
    ("5","Masters"),
    ("6","PhD"),
)

SPACING_CHOICES = (
    ("1","Select Spacing"),
    ("2","Double Spacing (2.0)"),
    ("3","Single Spacing (1.0)"),
)

DAYS_CHOICES = (
    ("1","Days"),
    ("2","1 Hour"),
    ("3","2 Hours"),
    ("4","3 Hours"),
    ("5","6 Hours"),
    ("6","12 Hours"),
    ("7","18 Hours"),
    ("8","1 Day"),
    ("9","2 Days"),
    ("10","3 Days"),
    ("11","4 Days"),
    ("12","5 Days"),
    ("13","6 Days"),
    ("14","7 Days"),
    ("15","12 Days"),
    ("16","15 Days"),
    ("17","18 Days"),
    ("18","20 Days"),
    ("19","25 Days"),
    ("20","1 Month"),
)
TYPE_CHOICES = (
    ("1","Select Type"),
    ("2","Admission essays"),
    ("3","Analysis of any type"),
    ("4","Capstone projects"),
    ("5","Coursework"),
    ("6","Dissertation"),
    ("7","Lab reports"),
    ("8","Presentations"),
    ("9","Research papers and proposals"),
    ("10","Speeches"),
    ("11","Other.."),
)

FORMAT_CHOICES = (
    ("1","Select Format"),
    ("2","MLA"),
    ("3","APA"),
    ("4","HARVAD"),
    ("5","OXFORD"),
    ("6","Other..")
)

PAGE_CHOICES = (
    ("1","Pages"),
    ("2","1 page"),
    ("3","2 pages"),
    ("4","3 pages"),
    ("5","4 pages"),
    ("6","5 pages"),
    ("7","6 pages"),
    ("8","7 pages"),
    ("9","8 pages"),
    ("10","9 pages"),
    ("11","10 pages"),
    ("12","11 - 15 pages"),
    ("13","16 - 20 pages"),
    ("14","21 - 30 pages"),
    ("15","Over 30 pages"),
)

class ContactForm(forms.Form):
    name = forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'name':'name','id':'name'}))
    email = forms.EmailField( label='',max_length=100 ,widget=forms.EmailInput(attrs={'name':'email','id':'email'}))
    message = forms.CharField( label='',widget=forms.Textarea(attrs={'id':'message','name':'message','rows':5}))

class OrderForm(forms.Form):
    name = forms.CharField(label='', max_length=100,widget=forms.TextInput)
    email = forms.EmailField( label='',max_length=100 ,widget=forms.EmailInput)
    academiclevel = forms.ChoiceField(label='',widget=forms.SelectMultiple,choices = ACADEMIC_LEVEL_CHOICES)
    subject = forms.ChoiceField(label='',widget=forms.SelectMultiple,choices=SUBJECT_CHOICES)
    pages = forms.ChoiceField(label='',widget=forms.SelectMultiple,choices=PAGE_CHOICES)
    days = forms.ChoiceField(label='', widget=forms.SelectMultiple,choices=DAYS_CHOICES)
    type = forms.ChoiceField(label='', widget=forms.SelectMultiple,choices=TYPE_CHOICES)
    format = forms.ChoiceField(label='', widget=forms.SelectMultiple,choices=FORMAT_CHOICES)
   
    
    instructions = forms.CharField( label='',widget=forms.Textarea(attrs={'rows':6,
                                                                            'place-holder':'Instructions...'
                                                                            }))

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

