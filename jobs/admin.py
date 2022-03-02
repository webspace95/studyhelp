from django.contrib import admin
from .models import Order, Sample, Writer
from django.contrib.auth.models import Group

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
	list_filter = ("writer",)

admin.site.register(Order,OrderAdmin)
admin.site.register(Sample)
admin.site.register(Writer)


admin.site.site_header = "Studyhelp Admin"