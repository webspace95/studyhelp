from django.db import models

# Create your models here.
# Middleware
def save_one_only(model_name):
    def save(self, *args, **kwargs):
        if not self.pk and model_name.objects.exists():
        # if you'll not check for self.pk 
        # then error will also raised in update of exists model
            raise ValidationError('There is can be only one '+model_name+' instance')
        return super(model_name, self).save(*args, **kwargs)


class HomeHeader(models.Model):

    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    
    save_one_only('HomeHeader')

    def __str__(self):
        return self.text

class HowWeWorkText(models.Model):

    introduction = models.TextField()
    body = models.TextField(blank=True,null=True)
    date = models.DateField(auto_now_add=True)

    save_one_only('HowWeWorkText')

    def __str__(self):
        return self.body[:50]



class BrandName(models.Model):

    text = models.CharField(max_length=20)

    save_one_only('BrandName')

    def __str__(self):
        return self.text

class GmailLink(models.Model):

    link = models.EmailField( max_length=254)

    save_one_only('GmailLink')

    def __str__(self):
        return self.link
    

class PhoneNumber(models.Model):

    name = models.TextField(default="phone number")
    phone = models.CharField(max_length=50)

    save_one_only('PhoneNumber')

    def __str__(self):
        return self.name
    

class TwitterAccount(models.Model):

    twitter = models.CharField(max_length=100)

    save_one_only('TwitterAccount')

    def __str__(self):
        return self.twitter

class FacebookAccount(models.Model):

    facebook = models.CharField(max_length=100)

    save_one_only('FacebookAccount')

    def __str__(self):
        return self.facebook   

class InstagramAccount(models.Model):

    ig = models.CharField(max_length=100)

    save_one_only('InstagramAccount')

    def __str__(self):
        return self.ig

class Address(models.Model):

    p_o_box = models.CharField( max_length=50)
    location = models.CharField(max_length=50)

    save_one_only('Address')

    def __str__(self):
        return self.p_o_box

class PrivacyPolicy(models.Model):

    name = models.CharField(max_length=50, default="privacy policy")
    body = models.TextField(default="")
    
    save_one_only('PrivacyPolicy')

    def __str__(self):
        return self.name
    
class RefundPolicy(models.Model):
    
    name = models.CharField(max_length=50, default="refund policy")
    heading = models.CharField( max_length=50)
    sub_heading = models.CharField( max_length=50)
    body = models.TextField()
    
    save_one_only('RefundPolicy')

    def __str__(self):
        return self.name

class AboutPage(models.Model):

    name = models.CharField(max_length=50,default="About page")
    heading = models.CharField(max_length=50)
    summary = models.CharField(max_length=50)
    subheading = models.CharField(max_length=50)
    body = models.TextField()

    save_one_only('AboutPage')

    def __str__(self):
        return self.name
    
class WhatsappNumber(models.Model):
    
    name = models.CharField(max_length=50,default="whatsapp")
    number = models.CharField(max_length=50)

    save_one_only('WhatsappNumber')

    def __str__(self):
        return self.name

class HowWeWorkCheckListItem(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

