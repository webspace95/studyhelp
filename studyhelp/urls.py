from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index_page),
    path(r'about/',views.about_view),
    path(r'privacy_policy/',views.privacy_policy),
    path(r'create_order/',views.create_order),
]
#appending the static files urls to the above media
urlpatterns += staticfiles_urlpatterns()
#how to upload media..appending the media url to the patterns above
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
