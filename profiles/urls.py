from django.urls import path
from . import views 


urlpatterns = [
    # profiles/urls.py

   path('', views.profile, name='profile'),  # Ensure 'profile' matches

   path('profile/edit/', views.edit_profile, name='edit_profile'),

   path('order/<int:id>/', views.profile_orders, name='profile_orders'),
   
   
]
    