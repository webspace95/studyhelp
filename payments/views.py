from django.shortcuts import render, HttpResponse, redirect, \
    get_object_or_404, reverse
from django.views.generic import ListView,DetailView,View
from django.contrib import messages

from django.conf import settings
from decimal import Decimal
from .models import Payment,Address
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import CheckoutForm
from paypal.standard.forms import PayPalPaymentsForm

from django.contrib import messages
from contacts.models import Whatsapp
from page_edits.models import GmailLink,InstagramAccount,TwitterAccount,FacebookAccount,PhoneNumber
from jobs.models import Order

# Create your views here.
#checkout view
@login_required()
def checkout_view(request,slug):

    order = Order.objects.get(reference_code=slug)
    gmail_links = GmailLink.objects.all()
    instagram_accounts = InstagramAccount.objects.all()
    fb_accounts = FacebookAccount.objects.all()
    twitter_accounts = TwitterAccount.objects.all()
    phone_numbers = PhoneNumber.objects.all()
    whatsapp = Whatsapp.objects.all()

    context = {
                'gmail_links':gmail_links,
                'instagram_accounts':instagram_accounts,
                'fb_accounts':fb_accounts,
                'twitter_accounts':twitter_accounts,
                'phone_numbers':phone_numbers,
                'whatsapp':whatsapp,
                'order':order,
              }

    if request.method == 'POST':
        form =CheckoutForm(request.POST)
        if form.is_valid():

            m_billing_address = form.cleaned_data['billing_address']
            m_billing_address2 = form.cleaned_data['billing_address2']
            m_billing_zip = form.cleaned_data['billing_zip']
    
            try:
                address = Address(
                                  user = request.user,
                                  street_address=m_billing_address,
                                  apartment_address=m_billing_address2,
                                  zip=m_billing_zip)
                address.save()

                messages.success(request,"Billing address saved succesfully")
                return redirect('/payments/payment/'+order.reference_code+'/')

            except Exception as e:
                messages.warning(request,"Please enter all the required fields")
                print(e)
                return redirect('/payments/checkout/'+order.reference_code+'/')
        else:
            messages.warning(request,"Plese complete all the required fields")
            print("exception occured or something")
            return redirect('/payments/checkout/'+order.reference_code+'/')
    else:
        form = CheckoutForm()
        context.update({
            'form':form
        })
    return render(request,'payments/checkout.htm',context)

@login_required()
def payment_view(request,slug):
    order = Order.objects.get(reference_code=slug)
    order_id = request.session.get('order_id')
    host = request.get_host()

    gmail_links = GmailLink.objects.all()
    instagram_accounts = InstagramAccount.objects.all()
    fb_accounts = FacebookAccount.objects.all()
    twitter_accounts = TwitterAccount.objects.all()
    phone_numbers = PhoneNumber.objects.all()
    whatsapp = Whatsapp.objects.all()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % order.price,
        'item_name': 'Order {}'.format(order.reference_code),
        'invoice': str(order.reference_code),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('payment_cancelled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)

    context = {
                'gmail_links':gmail_links,
                'instagram_accounts':instagram_accounts,
                'fb_accounts':fb_accounts,
                'twitter_accounts':twitter_accounts,
                'phone_numbers':phone_numbers,
                'whatsapp':whatsapp,
                'order':order,
                'form':form,
              }
    return render(request,'payments/payment.htm',context)



@csrf_exempt
def payment_done(request):
    return render(request, 'payments/payment_done.htm')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'payments/payment_cancelled.htm')