from django.contrib import admin
from .models import Order, Sample

# Register your models here.

admin.site.register(Order)
admin.site.register(Sample)

admin.site.site_header = "Studyhelp Admin"