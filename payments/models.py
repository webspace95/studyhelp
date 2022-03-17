from django.db import models
from django.conf import settings
# Create your models here.

class Address(models.Model):
    name = models.CharField( max_length=100)
    email = models.EmailField( max_length=254)
    postal_code = models.CharField( max_length=50)
    address = models.CharField( max_length=50)
    zip = models.CharField( max_length=50)

    def __str__(self):
        return self.email

class Payment(models.Model):
    #remember to put filter by user
    paypal_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,blank=True,null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    address = models.ForeignKey(Address,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.user.username
        
