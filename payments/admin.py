from django.contrib import admin
from .models import Payment,Address
# Register your models here.


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('charge_id','user','amount','timestamp')
    list_filter = ('user','timestamp')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('user','street_address','apartment_address','zip')
    list_filter = ('user',)

admin.site.register(Payment,PaymentAdmin)
admin.site.register(Address,AddressAdmin)