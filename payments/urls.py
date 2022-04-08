from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .import views

urlpatterns = [
    path('checkout/<slug>/',views.checkout_view),
    path('payment/<slug>/',views.payment_view),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
]
