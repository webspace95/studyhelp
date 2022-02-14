from django.db import models

# Create your models here.
class Section(models.Model):
    heading = models.CharField(max_length=256)
    body = models.TextField()

    def __str__(self):
        return self.heading
    