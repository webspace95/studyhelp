from django.db import models

# Create your models here.
#contact model
class Contact (models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    #snippet utils
    def __str__(self):
        return self.name

class Email(models.Model):

    email = models.EmailField(max_length=254)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
    
