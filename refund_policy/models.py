from django.db import models


# Create your models here.

class RefundPolicyIntroduction(models.Model):
    name = models.CharField(default="Introduction", max_length=50)
    body = models.TextField()

    
    def __str__(self):
        return self.name

class OrderCancelation(models.Model):
    question = models.CharField( max_length=256)
    answer = models.TextField()

    def __str__(self):
        return self.question

class DoubleCharge(models.Model):
    question = models.CharField( max_length=256)
    answer = models.TextField()

    def __str__(self):
        return self.question

class ShortageOfWriter(models.Model):
    question = models.CharField( max_length=256)
    answer = models.TextField()

    def __str__(self):
        return self.question

class RevisionDeadline(models.Model):
    question = models.CharField(max_length=256)
    answer = models.TextField()

    def __str__(self):
        return self.question

class Quality(models.Model):
    question = models.CharField( max_length=256)
    answer = models.TextField()

    def __str__(self):
        return self.question

    
    
    
    

    