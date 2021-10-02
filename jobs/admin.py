from django.contrib import admin
from .models import Order, OrderFile, CancelledOrder, CompletedOrder, CurrentOrder, Sample
# Register your models here.
admin.site.register(Order)
admin.site.register(CurrentOrder)
admin.site.register(CancelledOrder)
admin.site.register(CompletedOrder)
admin.site.register(OrderFile)
admin.site.register(Sample)
admin.site.site_header = "Studyhelp Admin"