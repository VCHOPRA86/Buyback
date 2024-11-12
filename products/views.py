from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Category, Brand, Product
from decimal import Decimal

def brand_products(request, brand_id):
    # View to list products filtered by brand
    brand = get_object_or_404(Brand, id=brand_id)
    products = Product.objects.filter(brand=brand)
    return render(request, 'products/brand_products.html', {
        'brand': brand,
        'products': products,
    })

def category_brands(request, category_id):
    # View to list brands within a given category
    category = get_object_or_404(Category, id=category_id)
    brands = Brand.objects.filter(category=category)
    return render(request, 'products/category_brands.html', {
        'category': category,
        'brands': brands,
    })


def category_list(request):
    # View to list all categories
    categories = Category.objects.all()
    return render(request, 'products/category_list.html', {'categories': categories})


def category_products(request, category_id):
    # Fetch category based on the category_id
    category = Category.objects.get(id=category_id)

    # Get all brands to populate the brand filter
    brands = Brand.objects.all()

    # Start with all products in the category
    products = Product.objects.filter(category=category)

    # Apply product filter if a product is selected
    selected_product_id = request.GET.get('products')
    if selected_product_id:
        products = products.filter(id=selected_product_id)

    # Apply brand filter if a brand is selected
    brand_filter = request.GET.get('brand')
    if brand_filter:
        products = products.filter(brand_id=brand_filter)

    # Render the template with the filtered products and brands
    return render(request, 'products/category_products.html', {
        'category': category,
        'brands': brands,
        'products': products
    })

def brand_list(request, category_id):
    # View to list brands for a given category
    category = get_object_or_404(Category, id=category_id)
    brands = category.brand_set.all()
    brands = Brand.objects.filter(category=category)
    return render(request, 'products/brand_list.html', {
        'category': category,
        'brands': brands,
    })

def product_list(request, category_id, brand_id):
    # View to list products filtered by category and brand
    category = get_object_or_404(Category, id=category_id)
    brand = get_object_or_404(Brand, id=brand_id)
    products = Product.objects.filter(category=category, brand=brand)
    return render(request, 'products/product_list.html', {
        'category': category,
        'brand': brand,
        'products': products,
    })

def product_detail(request, pk):
    # View to display product details
    product = get_object_or_404(Product, pk=pk)
    
    # Check if network selection is required for this product
    is_network_required = product.category.name.lower() == 'phone'

    if request.method == 'POST':
        # Handle dynamic price update based on condition and network status
        import json
        data = json.loads(request.body)
        condition = data.get('condition', 'working')
        network_status = data.get('network_status', 'unlocked')
        updated_price = product.get_price_by_condition_and_network(condition, network_status)
        return JsonResponse({'updated_price': str(updated_price)})

    # Render the product detail page
    return render(request, 'products/product_detail.html', {
        'product': product,
        'price': product.working_price,
        'is_network_required': is_network_required,
    })

def search_results(request):
    search_query = request.GET.get('search', '')  # Get the search query from the GET request
    products = Product.objects.filter(name__icontains=search_query)  # Case-insensitive search by product name
    
    if request.is_ajax():  # Check if the request is AJAX (for JSON response)
        products_data = [{'id': product.id, 'name': product.name} for product in products]
        return JsonResponse({'products': products_data, 'search_query': search_query})
    
    # If it's not an AJAX request, render the results in a template
    return render(request, 'products/search_results.html', {
        'search_query': search_query,
        'products': products,
    })

def search_products(request):
    search_query = request.GET.get('search', '')
    if search_query:
        products = Product.objects.filter(name__icontains=search_query)
        products_data = []
        for product in products:
            products_data.append({
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'image_url': product.image.url if product.image else None,
            })
        return JsonResponse({'products': products_data})
    return JsonResponse({'products': []})
    
