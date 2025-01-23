from django.shortcuts import render
from revieworder.models import Cart
from products.models import Category, Brand, Product
from django.http import JsonResponse
from allauth.account.forms import LoginForm



def base_view(request):
    cart_items = Cart.objects.all()  # Fetch cart items for global access
    return render(request, 'base.html', {'cart_items': cart_items})

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

# Terms & conditions
def terms(request):
    return render(request, 'home/terms.html')

# Privacy policy
def policy(request):
    return render(request, 'home/policy.html')


def autocomplete_products(request):
    # Get the search query parameter
    query = request.GET.get('search', '')

    # If there's a query, filter the products by name
    if query:
        products = Product.objects.filter(name__icontains=query)  # Case-insensitive search
        product_data = [{'id': product.id, 'name': product.name, 'slug': product.slug} for product in products]
    else:
        product_data = []

    return JsonResponse({'products': product_data})




