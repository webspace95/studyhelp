from django.shortcuts import get_object_or_404
from .models import Payment, Address
from jobs.models import Order
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver

def create_charge_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))

@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        # payment was successful
        order = Order.objects.get(reference_code=ipn.invoice)

        if order.price == ipn.mc_gross:
            # mark the order as paid
            order.payment_complete = 'T'
            order.save()

            charge = create_charge_id()
            charge = charge.upper()

            payment = Payment(
                charge_id=charge,
                user=order.user,
                amount=order.price
            )
            payment.save()
