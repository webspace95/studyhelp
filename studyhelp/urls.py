from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index_page),
    path(r'about/',views.about_view),
    path(r'privacy_policy/',views.privacy_policy),
    path(r'refund_policy/',views.refund_policy),
    path(r'terms_of_use/',views.terms_of_use),
    path(r'create_order/',views.create_order),
]

