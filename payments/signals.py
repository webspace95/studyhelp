from django.shortcuts import get_object_or_404
from jobs.models import Order
from .models import Payment
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
import random
import string

def generate_paypal_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))

@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        # payment was successful
        order = get_object_or_404(Order, id=ipn.invoice)

        if order.price == ipn.mc_gross:
            # mark the order as paid
            order.payment_complete = 'T'
            order.save()

            # create a payment
            payment = Payment(paypal_charge_id=generate_paypal_id(),user=order.user,amount=order.price,address=order.address)