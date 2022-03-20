from django.shortcuts import render, HttpResponse, redirect, \
    get_object_or_404, reverse
from django.views.generic import ListView,DetailView,View
from django.contrib import messages

from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from .models import Payment
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import CheckoutForm

from django.contrib import messages
from contacts.models import Whatsapp
from page_edits.models import Address,GmailLink,InstagramAccount,TwitterAccount,FacebookAccount,PhoneNumber
from jobs.models import Order

# Create your views here.
#checkout view
@login_required()
def checkout_view(request,slug):

    order = Order.objects.get(reference_code=slug)
    addresses = Address.objects.all()
    gmail_links = GmailLink.objects.all()
    instagram_accounts = InstagramAccount.objects.all()
    fb_accounts = FacebookAccount.objects.all()
    twitter_accounts = TwitterAccount.objects.all()
    phone_numbers = PhoneNumber.objects.all()
    whatsapp = Whatsapp.objects.all()

    context = {
                'addresses':addresses,
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
    
            try:
                address = Address(name=m_name,email=email_address,postal_code=m_postal_code,address=m_address,zip=m_zip)
                address.save()

                order.address = address
                order.save()
                
                request.session['order_id'] = order.id
                return redirect('/payments/process-payment/')

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


def process_payment(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % order.price.quantize(
            Decimal('.01')),
        'item_name': 'Order {}'.format(order.id),
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('payment_cancelled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payments/process_payment.htm', {'order': order, 'form': form})

@csrf_exempt
def payment_done(request):
    return render(request, 'payments/payment_done.htm')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'payments/payment_cancelled.htm')
