from django.db import models
from django.conf import settings

STATUS_CHOICES = (
    ('IP', 'inprogress'),
    ('CP', 'Completed'),
    ('CN', 'Cancelled'),
)

# Create your models here.
class Order(models.Model):
    #meta
    name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    academic_level = models.CharField( max_length=50)
    subject = models.CharField(max_length=50)
    number_of_pages = models.CharField(max_length=50)
    days = models.CharField(max_length=50)
    type = models.CharField( max_length=50)
    paper_format = models.CharField( max_length=50)
    instructions = models.TextField(default="")
 
    #order status
    status = models.CharField(choices=STATUS_CHOICES,max_length=2,blank=True,null=True)

    #date ields
    date_created = models.DateTimeField(auto_now_add=True)

    #user field
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, blank=True,null=True)

    #refrence code
    reference_code = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.name


class Sample(models.Model):
    
    title = models.CharField( max_length=50)
    description = models.TextField(blank=True)
    no_of_pages = models.IntegerField(blank=True,null=True)
    format = models.CharField(max_length=50,blank=True,null=True)
    subject = models.CharField(max_length=50,blank=True,null=True)
    file = models.FileField(max_length=100,blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.description[:50]