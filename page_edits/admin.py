from django.contrib import admin
from .models import HomeHeader,BrandName,GmailLink,PhoneNumber,TwitterAccount,FacebookAccount,InstagramAccount,Address,AboutPage
# Register your models here.

admin.site.register(HomeHeader)
admin.site.register(BrandName)
admin.site.register(GmailLink)
admin.site.register(PhoneNumber)
admin.site.register(TwitterAccount)
admin.site.register(FacebookAccount)
admin.site.register(InstagramAccount)
admin.site.register(Address)
admin.site.register(AboutPage)
