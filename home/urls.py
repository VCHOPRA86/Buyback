from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sell-mobile/', views.sell_mobile, name='sell_mobile'),
    path('how-it-works/', views.how_it_works, name='how_it_works'),
    path('why-use-us/', views.why_use_us, name='why_use_us'),
    path('support/', views.support, name='support'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('autocomplete-products/', views.autocomplete_products, name='autocomplete_products'),
    

]
