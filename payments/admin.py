from django.contrib import admin
from .models import Payment,Address
# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
    list_filter = ("user",)

admin.site.register(Payment,PaymentAdmin)
admin.site.register(Address)