from django.contrib import admin
from .models import HomeHeader,HowWeWorkText,BrandName,GmailLink,PhoneNumber,TwitterAccount,FacebookAccount,InstagramAccount,Address,PrivacyPolicy,RefundPolicy,AboutPage,WhatsappNumber,HowWeWorkCheckListItem
# Register your models here.

admin.site.register(HomeHeader)
admin.site.register(HowWeWorkText)
admin.site.register(BrandName)
admin.site.register(GmailLink)
admin.site.register(PhoneNumber)
admin.site.register(TwitterAccount)
admin.site.register(FacebookAccount)
admin.site.register(InstagramAccount)
admin.site.register(Address)
admin.site.register(PrivacyPolicy)
admin.site.register(RefundPolicy)
admin.site.register(AboutPage)
admin.site.register(WhatsappNumber)
admin.site.register(HowWeWorkCheckListItem)

'''
At launch we will activate this code
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    readonly_fields = [
        'date_joined',
    ]
'''