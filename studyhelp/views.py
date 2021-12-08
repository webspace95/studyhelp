from django.shortcuts import render,redirect
from .forms import ContactForm, OrderForm
from django.conf import settings
from contacts.models import Contact, UserProfile,Whatsapp
from jobs.models import Order, Sample
from seo.models import AboutMetaField,AboutTitleField,SampleMetaField,SampleTitleField,IndexMetaField,IndexTitleField,PrivacypolicyMetaField,PrivacypolicyTitleField,OrderMetaField,OrderTitleField,DashboardMetaField,DashboardTitleField
from page_edits.models import HomeHeader,HowWeWorkCheckListItem,HowWeWorkText,BrandName,Address,GmailLink,InstagramAccount,TwitterAccount,FacebookAccount,PrivacyPolicy,PhoneNumber,AboutPage
from django.contrib import messages
from services.models import AssignmentWritingService, DissertationAndThesisHelp, ProofReadingService, ContentWritingService


def create_ref_code():
    return 'ODR'.join(random.choices(string.ascii_lowercase + string.digits, k=7))

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
    whatsapp = Whatsapp.objects.all()

    index_title = IndexTitleField.objects.all()
    index_meta = IndexMetaField.objects.all()

    dissertations = DissertationAndThesisHelp.objects.all()
    assignments = AssignmentWritingService.objects.all()
    proofreadings = ProofReadingService.objects.all()
    contents = ContentWritingService.objects.all()
    
    context = {
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
                'dissertations':dissertations,
                'proofreadings':proofreadings,
                'contents':contents,
                'assignments':assignments,
                'whatsapp':whatsapp,
                'index_title':index_title,
                'index_meta':index_meta
              }

    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            
            #getting values of the form field
            m_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']
        
            try:
                contact = Contact(name=m_name,email=email_address,message=mail_message)
                contact.save()
                messages.success(request,"Message sent succesfully.")
                return redirect('/')

            except Exception as e:
                messages.warning(request,"Please enter all the required fields")
                return redirect('/')
        else:
            messages.warning(request,"Plese complete all the required fields")
            return redirect('/')
    else:
        form = ContactForm()
        context.update({
            'form':form
        })
    return render(request,'index.htm',context)

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
    whatsapp = Whatsapp.objects.all()

    about_title = AboutTitleField.objects.all()
    about_meta = AboutMetaField.objects.all()

    context = {
                'samples':samples,
                'addresses':addresses,
                'gmail_links':gmail_links,
                'instagram_accounts':instagram_accounts,
                'fb_accounts':fb_accounts,
                'twitter_accounts':twitter_accounts,
                'phone_numbers':phone_numbers,
                'abouts':abouts,
                'whatsapp':whatsapp,
                'about_title':about_title,
                'about_meta':about_meta
              }

    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            
            #getting values of the form field
            m_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']
        
            try:
                contact = Contact(name=m_name,email=email_address,message=mail_message)
                contact.save()
                messages.success(request,"Message sent succesfully.")
                return redirect('/about/')

            except Exception as e:
                messages.warning(request,"Please enter all the required fields")
                return redirect('/about/')
        else:
            messages.warning(request,"Plese complete all the required fields")
            return redirect('/about/')
    else:
        form = ContactForm()
        context.update({
            'form':form
        })
    return render(request,'about.htm',context)

def privacy_policy(request):

    addresses = Address.objects.all()
    gmail_links = GmailLink.objects.all()
    instagram_accounts = InstagramAccount.objects.all()
    fb_accounts = FacebookAccount.objects.all()
    twitter_accounts = TwitterAccount.objects.all()
    phone_numbers = PhoneNumber.objects.all()
    privacy_policies = PrivacyPolicy.objects.all()
    whatsapp = Whatsapp.objects.all()

    privacy_title = PrivacypolicyTitleField.objects.all()
    privacy_meta = PrivacypolicyMetaField.objects.all()


    context = {
            'addresses':addresses,
            'gmail_links':gmail_links,
            'instagram_accounts':instagram_accounts,
            'fb_accounts':fb_accounts,
            'twitter_accounts':twitter_accounts,
            'phone_numbers':phone_numbers,
            'privacy_policies':privacy_policies,
            'whatsapp':whatsapp,
            'privacy_title':privacy_title,
            'privacy_meta':privacy_meta
            }

    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            
            #getting values of the form field
            m_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']
        
            try:
                contact = Contact(name=m_name,email=email_address,message=mail_message)
                contact.save()
                messages.success(request,"Message sent succesfully.")
                return redirect('/privacy_policy/')

            except Exception as e:
                messages.warning(request,"Please enter all the required fields")
                return redirect('/privacy_policy/')
        else:
            messages.warning(request,"Plese complete all the required fields")
            return redirect('/privacy_policy/')
    else:
        form = ContactForm()
        context.update({
            'form':form
        })
    return render(request,'privacy_policy.htm',context)

def create_order(request):
    headers = HomeHeader.objects.all().order_by('date')
    brands = BrandName.objects.all()
    how_we_work_texts = HowWeWorkText.objects.all()
    addresses = Address.objects.all()
    gmail_links = GmailLink.objects.all()
    instagram_accounts = InstagramAccount.objects.all()
    fb_accounts = FacebookAccount.objects.all()
    twitter_accounts = TwitterAccount.objects.all()
    phone_numbers = PhoneNumber.objects.all()
    steps = HowWeWorkCheckListItem.objects.all()
    whatsapp = Whatsapp.objects.all()
    order_title = OrderTitleField.objects.all()
    order_meta = OrderMetaField.objects.all()

    context = {
        'headers':headers,
        'brands':brands,
        'how_we_work_texts':how_we_work_texts,
        'addresses':addresses,
        'gmail_links':gmail_links,
        'instagram_accounts':instagram_accounts,
        'fb_accounts':fb_accounts,
        'twitter_accounts':twitter_accounts,
        'phone_numbers':phone_numbers,
        'steps':steps,
        'whatsapp':whatsapp,
        'order_title':order_title,
        'order_meta':order_meta
    }

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            m_name = form.cleaned_data['name']
            m_email = form.cleaned_data['email']
            m_academiclevel = form.cleaned_data['academiclevel'].option.value
            m_subject = form.cleaned_data['subject'].option.value
            m_pages = form.cleaned_data['pages'].option.value
            m_days = form.cleaned_data['days'].option.value
            m_type = form.cleaned_data['type'].option.value
            m_format = form.cleaned_data['format'].option.value
            m_instructions = form.cleaned_data['instructions']

            #refrence code and status
            m_status='IP'
            ref_code = create_ref_code()

            try:
                order = Order(name=m_name,
                              email=m_email,
                              academic_level=m_academiclevel,
                              subject=m_subject,
                              number_of_pages=m_pages,
                              days=m_days,
                              type=m_type,
                              paper_format=m_format,
                              instructions=m_instructions,
                              status=m_status,
                              user=request.user,
                              reference_code=ref_code)
                print(order)
                order.save()
                return redirect('/create_order/')
            except Exception as e:
                print("an error occured. yoww dumbbb")
                return redirect('/create_order/')
        else:
            print("an error occured")
            return redirect('/create_order/')
    else:
        form = OrderForm()
        context.update(
            {'form':form}
        )
    return render(request,'create_order.htm',context)

def samples(request):
    samples = Sample.objects.all()
    headers = HomeHeader.objects.all().order_by('date')
    brands = BrandName.objects.all()
    whatsapp = Whatsapp.objects.all()
    addresses = Address.objects.all()
    gmail_links = GmailLink.objects.all()
    instagram_accounts = InstagramAccount.objects.all()
    fb_accounts = FacebookAccount.objects.all()
    twitter_accounts = TwitterAccount.objects.all()
    phone_numbers = PhoneNumber.objects.all()
    sample_title = SampleTitleField.objects.all()
    sample_meta = SampleMetaField.objects.all()


    context = {
            'samples':samples,
            'headers':headers,
            'brands':brands,
            'whatsapp':whatsapp,
            'phone_numbers':phone_numbers,
            'gmail_links':gmail_links,
            'instagram_accounts':instagram_accounts,
            'fb_accounts':fb_accounts,
            'twitter_accounts':twitter_accounts,
            'addresses':addresses,
            'sample_title':sample_title,
            'sample_meta':sample_meta
        }

    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            
            #getting values of the form field
            m_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']
        
            try:
                contact = Contact(name=m_name,email=email_address,message=mail_message)
                contact.save()
                messages.success(request,"Message sent succesfully.")
                return redirect('/samples/')

            except Exception as e:
                messages.warning(request,"Please enter all the required fields")
                return redirect('/samples/')
        else:
            messages.warning(request,"Plese complete all the required fields")
            return redirect('/samples/')
    else:
        form = ContactForm()
        context.update({
            'form':form
        })
    return render(request,"samples.htm",context)

def dashboard(request):
    headers = HomeHeader.objects.all().order_by('date')
    brands = BrandName.objects.all()
    addresses = Address.objects.all()
    gmail_links = GmailLink.objects.all()
    instagram_accounts = InstagramAccount.objects.all()
    fb_accounts = FacebookAccount.objects.all()
    twitter_accounts = TwitterAccount.objects.all()
    phone_numbers = PhoneNumber.objects.all()
    completed_orders = Order.objects.filter(user=request.user,status='Completed')
    current_orders = Order.objects.filter(user=request.user,status='inprogress')
    whatsapp = Whatsapp.objects.all()
    dashboard_title = DashboardTitleField.objects.all()
    dashboard_meta = DashboardMetaField.objects.all()

    context = {
        'headers':headers,
        'brands':brands,
        'addresses':addresses,
        'gmail_links':gmail_links,
        'instagram_accounts':instagram_accounts,
        'fb_accounts':fb_accounts,
        'twitter_accounts':twitter_accounts,
        'phone_numbers':phone_numbers,
        'completed_orders':completed_orders,
        'current_orders':current_orders,
        'whatsapp':whatsapp,
        'dadhboard_title':dashboard_title,
        'dashboard_meta':dashboard_meta
    }

    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            
            #getting values of the form field
            m_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']
        
            try:
                contact = Contact(name=m_name,email=email_address,message=mail_message)
                contact.save()
                messages.success(request,"Message sent succesfully.")
                return redirect('/dashboard/')

            except Exception as e:
                messages.warning(request,"Please enter all the required fields")
                return redirect('/dashboard/')
        else:
            messages.warning(request,"Plese complete all the required fields")
            return redirect('/dashboard/')
    else:
        form = ContactForm()
        context.update({
            'form':form
        })
    return render(request,'dashboard.htm',context)