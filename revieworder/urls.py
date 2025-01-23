from django.urls import path
from . import views 

app_name = 'revieworder'


urlpatterns = [
    path('add-to-cart/<slug:product_slug>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('', views.revieworder, name='revieworder'),  # Ensure this line exists
]