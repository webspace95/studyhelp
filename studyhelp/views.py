from django.shortcuts import render,redirect
from .forms import ContactForm, OrderForm
from contacts.models import Contact
from jobs.models import Order,OrderFile, CancelledOrder, CompletedOrder, CurrentOrder
from .mailservice import send_contact_email,send_contact_notification,send_order_email,send_order_notification
from page_edits.models import HomeHeader

def index_page(request):
    headers = HomeHeader.objects.all().order_by('date')
    if request.method == 'POST':
        form =ContactForm(request.POST)

        if form.is_valid():
            
            #getting values of the form field
            m_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']
        

            # saving the contacts
            # sending an email and an sms notification
            send_contact_email(email_address)
            send_contact_notification(email_address, mail_message)
            contact = Contact(name=m_name,email=email_address,message=mail_message)
            contact.save()
            return redirect('/')
    else:
        form = ContactForm()
    return render(request,'index.htm',{'form':form,'headers':headers})

#about view
def about_view(request):
    if request.method == 'POST':
        form =ContactForm(request.POST)

        if form.is_valid():
            
            #getting values of the form field
            m_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']
        
            # saving the contacts
            # sending an email and an sms notification
            send_contact_email(email_address)
            send_contact_notification(email_address, mail_message)
            contact = Contact(name=m_name,email=email_address,message=mail_message)
            contact.save()
            return redirect('/about/')
    else:
        form = ContactForm()
    return render(request,'about.htm',{'form':form})

def privacy_policy(request):
    if request.method == 'POST':
        form =ContactForm(request.POST)

        if form.is_valid():
            
            #getting values of the form field
            m_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']
        
            # saving the contacts
            # sending an email and an sms notification
            send_contact_email(email_address)
            send_contact_notification(email_address, mail_message)
            contact = Contact(name=m_name,email=email_address,message=mail_message)
            contact.save()
            return redirect('/privacy_policy/')
    else:
        form = ContactForm()
    return render(request,'privacy_policy.htm',{'form':form})

def refund_policy(request):
    if request.method == 'POST':
        form =ContactForm(request.POST)

        if form.is_valid():
            
            #getting values of the form field
            m_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']
        
            # saving the contacts
            # sending an email and an sms notification
            send_contact_email(email_address)
            send_contact_notification(email_address, mail_message)
            contact = Contact(name=m_name,email=email_address,message=mail_message)
            contact.save()
            return redirect('/refund_policy/')
    else:
        form = ContactForm()
    return render(request,'refund_policy.htm',{'form':form})

def terms_of_use(request):
    if request.method == 'POST':
        form =ContactForm(request.POST)

        if form.is_valid():
            
            #getting values of the form field
            m_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']
        
            # saving the contacts
            # sending an email and an sms notification
            send_contact_email(emai_address)
            send_contact_notification(email_address, mail_message)
            contact = Contact(name=m_name,email=email_address,message=mail_message)
            contact.save()
            return redirect('/terms_of_use/')
    else:
        form = ContactForm()
    return render(request,'about.htm',{'form':form})

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():

            m_name = form.cleaned_data['name']
            m_email = form.cleaned_data['email']
            m_title = form.cleaned_data['title']
            m_pages = form.cleaned_data['pages']
            m_deadline = form.cleaned_data['deadline']
            m_type = form.cleaned_data['type']
            m_format = form.cleaned_data['format']
            m_subject = form.cleaned_data['subject']
            m_academiclevel = form.cleaned_data['academiclevel']
            m_instructions = form.cleaned_data['message']


            send_order_email(m_email)
            send_order_notification(m_email, m_instructions)
            order = Order(name = m_name,
                          email = m_email,
                          subject = m_subject,
                          number_of_pages = m_pages,
                          education_level = m_academiclevel,
                          type = m_type,
                          paper_format = m_format,
                          order_inprogress = True,
                          order_completed = False,
                          order_cancelled = False,
                          deadline = m_deadline,
                          title = m_title)
            order.save()
            return redirect('/create_order/')
    else:
        form = OrderForm()
    return render(request,'create_order.htm',{'form':form})