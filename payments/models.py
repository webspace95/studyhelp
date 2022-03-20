from django.db import models
from django.conf import settings
# Create your models here.

class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,blank=True,null=True)
    street_address = models.CharField(max_length=100,blank=True,null=True)
    apartment_address = models.CharField(max_length=100,blank=True,null=True)
    zip = models.CharField(max_length=100)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Payment(models.Model):
    charge_id = models.CharField(max_length=50,blank=True,null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
        
