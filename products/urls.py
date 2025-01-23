from django.urls import path
from . import views


urlpatterns = [
    path('/', views.category_list, name='category_list'),
    path('<slug:category_slug>', views.brand_list, name='category_brands'),
    path('category/<slug:category_slug>', views.category_products, name='category_products'),
    path('<slug:category_slug>/<slug:brand_slug>', views.product_list, name='brand_products'),
    path('sell/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search_results, name='search_results'),
    path('search-products/<slug:product_slug>', views.search_products, name='search_products'),


]

