from django.shortcuts import render,redirect
from .forms import ContactForm, OrderForm
from contacts.models import Contact, Email
from jobs.models import Order,OrderFile, CancelledOrder, CompletedOrder, CurrentOrder, Sample
from .mailservice import send_contact_email,send_contact_notification,send_order_email,send_order_notification
from page_edits.models import HomeHeader,HowWeWorkText,BrandName,Address,GmailLink,InstagramAccount,TwitterAccount,FacebookAccount,PhoneNumber,AboutPage
from django.contrib import messages
from services.models import AssignmentWritingService, DissertationAndThesisHelp, ProofReadingService, ContentWritingService
def index_page(request):

    headers = HomeHeader.objects.all().order_by('date')
    how_we_work_texts = HowWeWorkText.objects.all()
    brands = BrandName.objects.all()
    samples = Sample.objects.all()
    addresses = Address.objects.all()
    gmail_links = GmailLink.objects.all()
    instagram_accounts = InstagramAccount.objects.all()
    fb_accounts = FacebookAccount.objects.all()
    twitter_accounts = TwitterAccount.objects.all()
    phone_numbers = PhoneNumber.objects.all()
    abouts = AboutPage.objects.all()

    disertations = DissertationAndThesisHelp.objects.all()
    assignments = AssignmentWritingService.objects.all()
    proofreadings = ProofReadingService.objects.all()
    contents = ContentWritingService.objects.all()
    
    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            
            #getting values of the form field
            m_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']
        
            try:
                # saving the contacts
                # sending an email and an sms notification
                send_contact_email(email_address)
                send_contact_notification(email_address, mail_message)

                email_qs = Email.objects.filter(email==email_address)
                if email_qs.exists():

                    contact = Contact(name=m_name,email=email_address,message=mail_message)
                    contact.save()
                    messages.info(request,"Message sent succesfully.Check your email for confirmation")
                    return redirect('/')
                else:
                    email = Email(email=email_address)
                    email.save()
                    contact = Contact(name=m_name,email=email_address,message=mail_message)
                    contact.save()
                    messages.info(request,"Message sent succesfully.Check your email for confirmation")
                    return redirect('/')

            except Exception as e:
                messages.warning(request,"Please enter a valid email address")
                return redirect('/')
        else:
            messages.warning(request,"Plese complete all the required fields")
            return redirect('/')
    else:
        form = ContactForm()
    return render(request,'index.htm',{
                                       'form':form,
                                       'headers':headers,
                                       'how_we_work_texts':how_we_work_texts,
                                       'brands':brands,
                                       'samples':samples,
                                       'addresses':addresses,
                                       'gmail_links':gmail_links,
                                       'instagram_accounts':instagram_accounts,
                                       'fb_accounts':fb_accounts,
                                       'twitter_accounts':twitter_accounts,
                                       'phone_numbers':phone_numbers,
                                       'disertations':disertations,
                                       'proofreadings':proofreadings,
                                       'contents':contents,
                                       'assignments':assignments
                                       })

#about view
def about_view(request):

    samples = Sample.objects.all()
    addresses = Address.objects.all()
    gmail_links = GmailLink.objects.all()
    instagram_accounts = InstagramAccount.objects.all()
    fb_accounts = FacebookAccount.objects.all()
    twitter_accounts = TwitterAccount.objects.all()
    phone_numbers = PhoneNumber.objects.all()
    abouts = AboutPage.objects.all()

    if request.method == 'POST':
        form =ContactForm(request.POST)

        if form.is_valid():
            
            #getting values of the form field
            m_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']

            try:
                # saving the contacts
                # sending an email and an sms notification
                send_contact_email(email_address)
                send_contact_notification(email_address, mail_message)
                
                email_qs = Email.objects.filter(email == email_address)
                if email_qs.exists():
                    contact = Contact(name=m_name,email=email_address,message=mail_message)
                    contact.save()
                    messages.info(request, "Message sent succesfully")
                    return redirect('/about/')
                else:
                    email = Email(email=email_address)
                    email.save()
                    contact = Contact(name=m_name,email=email_address,message=mail_message)
                    contact.save()
                    messages.info(request, "Message sent succesfully")
                    return redirect('/about/')
            except Exception as e:
                messages.warning(request,"Please enter a valid email address")
                return redirect('/about/')
        else:
            messages.warning(request,"Please complete all the required fields")
            return redirect('/about/')
    else:
        form = ContactForm()
    return render(request,'about.htm',{
                                       'form':form,
                                       'samples':samples,
                                       'addresses':addresses,
                                       'gmail_links':gmail_links,
                                       'instagram_accounts':instagram_accounts,
                                       'fb_accounts':fb_accounts,
                                       'twitter_accounts':twitter_accounts,
                                       'phone_numbers':phone_numbers,
                                       'abouts':abouts,
                                       })

def privacy_policy(request):

    addresses = Address.objects.all()
    gmail_links = GmailLink.objects.all()
    instagram_accounts = InstagramAccount.objects.all()
    fb_accounts = FacebookAccount.objects.all()
    twitter_accounts = TwitterAccount.objects.all()
    phone_numbers = PhoneNumber.objects.all()

    if request.method == 'POST':
        form =ContactForm(request.POST)

        if form.is_valid():
            
            #getting values of the form field
            m_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']
            try:
                # saving the contacts
                # sending an email and an sms notification
                send_contact_email(email_address)
                send_contact_notification(email_address, mail_message)
                contact = Contact(name=m_name,email=email_address,message=mail_message)
                contact.save()
                messages.info(request,"Message sent succesfully. Check your email for confirmation")
                return redirect('/privacy_policy/')

            except Exception as e:
                messages.warning(request,"Please enter a valid email address")
                return redirect('/privacy_policy/')
        
        else:
            messages.warning(request,"Please enter all the required fields")
            return redirect('/privacy_policy/')
    else:
        form = ContactForm()
    return render(request,'privacy_policy.htm',{
                                       'form':form,
                                       'addresses':addresses,
                                       'gmail_links':gmail_links,
                                       'instagram_accounts':instagram_accounts,
                                       'fb_accounts':fb_accounts,
                                       'twitter_accounts':twitter_accounts,
                                       'phone_numbers':phone_numbers
                                       })

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

            try:
                email_qs = Email.objects.filter(email ==m_email)
                if email_qs.exists():
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
                    messages.success(request,"Order created succesfully! check your email for confirmation ")
                    messages.success(request,"You can communicate with us via email for more instructions and tracking your order")
                    return redirect('/create_order/')
                else:
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
                    email = Email(email = m_email)
                    email.save()
                    messages.success(request,"Order created succesfully! check your email for confirmation ")
                    messages.success(request,"You can communicate with us via email for more instructions and tracking your order")
                    return redirect('/create_order/')
            except Exception as e:
                messages.warning(request,"Please enter a valid email address")
                return redirect('/create_order/')
        else:
            messages.warning(request,"Please complete all the required fields")
            return redirect('/create_order/')
    else:
        form = OrderForm()
    return render(request,'create_order.htm',{'form':form})

def samples(request):
    samples = Sample.objects.all()
    headers = HomeHeader.objects.all().order_by('date')
    brands = BrandName.objects.all()

    if request.method == 'POST':
        form = ContactForm()
        if form.is_valid():

            m_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']

            try:
                email_qs = Email.objects.filter(email == email_address)
                if email_qs.exists():
                    send_contact_email(email_address)
                    send_contact_notification(email_address, mail_message)
                    contact = Contact(name=m_name,email=email_address,message=mail_message)
                    contact.save()
                    messages.info(request,"Message sent succesfully. Check your email for confirmation")
                    return redirect('/samples/')
                else:
                    email = Email(email=email_address)
                    email.save()
                    send_contact_email(email_address)
                    send_contact_notification(email_address, mail_message)
                    contact = Contact(name=m_name,email=email_address,message=mail_message)
                    contact.save()
                    messages.info(request,"Message sent succesfully. Check your email for confirmation")
                    return redirect('/samples/')
            except Exception as e:
                messages.warning(request,"Please enter a valid email address")
                return redirect('/samples/')
        else:
            messages.warning(request,"Please complete the required fields")
            return redirect('/samples/')
    else:
        form = ContactForm()
        return render(request,"samples.htm",{
            'samples':samples,
            'headers':headers,
            'brands':brands,
            'form':form,
        })