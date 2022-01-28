from django.contrib import admin
from .models import Order, Sample
from django.contrib.auth.models import Group

# Register your models here.

admin.site.register(Order)
admin.site.register(Sample)
admin.site.unregister(Group)


admin.site.site_header = "Studyhelp Admin"