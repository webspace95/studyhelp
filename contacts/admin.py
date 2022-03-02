from django.contrib import admin

# Register your models here.
from .models import Contact,UserProfile,Whatsapp


class ContactAdmin(admin.ModelAdmin):
    list_filter = ("date",)
    
admin.site.register(Contact,ContactAdmin)
admin.site.register(Whatsapp)