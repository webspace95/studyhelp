from django.db import models

# Create your models here.
class Order(models.Model):
    #meta
    name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    subject = models.TextField()
    number_of_pages = models.IntegerField()
    education_level = models.CharField( max_length=50)
    type = models.CharField( max_length=50)
    paper_format = models.CharField( max_length=50)
 
    #bool fields
    order_inprogress = models.BooleanField()
    order_completed = models.BooleanField()
    order_cancelled = models.BooleanField()

    #date ields
    deadline = models.DateTimeField(auto_now_add=False)
    date_created = models.DateTimeField(auto_now_add=True)

    title = models.CharField( max_length=50)


    def __str__(self):
        return self.name

class CurrentOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.order.name

class CompletedOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.order.name    

class CancelledOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.order.name
    

class OrderFile(models.Model):
    order_file = models.FileField( max_length=100)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.order.name


class Sample(models.Model):
    
    title = models.CharField( max_length=50)
    description = models.TextField(blank=True)
    no_of_pages = models.IntegerField(blank=True,null=True)
    format = models.CharField(max_length=50,blank=True,null=True)
    discipline = models.CharField(max_length=50,blank=True,null=True)
    file = models.FileField(max_length=100,blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.description[:50]