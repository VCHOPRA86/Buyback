from django.conf import settings
from django.shortcuts import render, get_object_or_404
from products.models import Category, Brand, Product
from django.http import JsonResponse


# The home view for rendering the home page
def home(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()  # Query the Brand model to get all brands
    return render(request, 'home/index.html', {'categories': categories, 'brands': brands })

# Additional views for static pages
def sell_mobile(request):
    categories = Category.objects.all()  # Fetch all categories
    brands = Brand.objects.all()  # Fetch all brands
    return render(request, 'home/sell_mobile.html', {'categories': categories, 'brands': brands})

def how_it_works(request):
    return render(request, 'home/how_it_works.html')

def why_use_us(request):
    return render(request, 'home/why_use_us.html')

def reviews(request):
    return render(request, 'home/reviews.html')

def support(request):
    return render(request, 'home/support.html')

def signup(request):
    return render(request, 'home/signup.html')

def login(request):
    return render(request, 'home/login.html')


def autocomplete_products(request):
    # Get the search query parameter
    query = request.GET.get('search', '')

    # If there's a query, filter the products by name
    if query:
        products = Product.objects.filter(name__icontains=query)  # Case-insensitive search
        product_data = [{'id': product.id, 'name': product.name} for product in products]
    else:
        product_data = []

    return JsonResponse({'products': product_data})