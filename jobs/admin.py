from django.contrib import admin
from .models import Order, Sample, Writer, OrderFile
from django.contrib.auth.models import Group

# Register your models here.

admin.site.register(Order)
admin.site.register(Sample)
admin.site.register(Writer)
admin.site.register(OrderFile)

admin.site.site_header = "Studyhelp Admin"