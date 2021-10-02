from django.contrib import admin

# Register your models here.
from .models import Contact,Email

admin.site.register(Contact)
admin.site.register(Email)