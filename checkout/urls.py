from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    
    path('', views.checkout, name='checkout'),
    path('confirm_sale/', views.confirm_sale, name='confirm_sale'),
    path('checkout_success/<str:order_number>/', views.checkout_success, name='checkout_success'),  # Ensure this pattern exists

]
