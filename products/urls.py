from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('products/category/<int:category_id>/brands/', views.brand_list, name='category_brands'),
    path('category/<int:category_id>/products/', views.category_products, name='category_products'),
    path('category/<int:category_id>/brand/<int:brand_id>/', views.product_list, name='brand_products'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('search/', views.search_results, name='search_results'),
    path('search-products/', views.search_products, name='search_products'),

]

