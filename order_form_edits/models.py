from django.db import models

# Create your models here.
class Page(models.Model):
    name = models.CharField( max_length=50)
    def __str__(self):
        return self.name
#subject
class Subject(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
#academic levels
class AcademicLevel(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

#spacing
class Spacing(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

#days
class Day(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

#type
class Type(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

#format
class Format(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

    