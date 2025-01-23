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


def category_products(request, category_slug):
    # Retrieve the category by its slug
    category = get_object_or_404(Category, slug=category_slug)

    # Get all brands to populate the brand filter
    brands = Brand.objects.filter(products__category=category).distinct()

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

def brand_list(request, category_slug):
    # View to list brands for a given category
    category = get_object_or_404(Category, slug=category_slug)
    brands = category.brand_set.all()
    brands = Brand.objects.filter(category=category)
    return render(request, 'products/brand_list.html', {
        'category': category,
        'brands': brands,
    })

def product_list(request, category_slug, brand_slug):
    # View to list products filtered by category and brand
    
    category = get_object_or_404(Category, slug=category_slug)
    brand = get_object_or_404(Brand, slug=brand_slug)
    products = Product.objects.filter(category=category, brand=brand)
    return render(request, 'products/product_list.html', {
        'category': category,
        'brand': brand,
        'products': products,
    })

def product_detail(request, product_slug):
    print(f"Product Slug: {product_slug}")  # Debugging the slug
    # Retrieve the product or return a 404
    product = get_object_or_404(Product, slug=product_slug)
    
    # Get all storage options for the product
    storage_options = product.storage_options.all()

    # Determine if network selection is required
    is_network_required = product.category.name.lower() in ['phones', 'tablets']


    if request.method == 'POST':
        # Handle dynamic price updates based on input
        import json
        data = json.loads(request.body)
        
        # Extract condition, network status, and storage size
        condition = data.get('condition', 'working')
        network = data.get('network', 'unlocked')
        storage_size = data.get('storage_size')

        print(f"Condition: {condition}, Network: {network}, Storage Size: {storage_size}")  # Debug individual fields
        
        # Calculate base price based on condition and network status
        updated_price = product.get_price_by_condition_and_network(condition, network)

        # Add price adjustment for selected storage size
        if storage_size:
            storage_option = product.storage_options.filter(size=storage_size).first()
            if storage_option:
                updated_price += storage_option.additional_price

        # Format the updated price to two decimal places
        formatted_price = "{:.2f}".format(updated_price)

        # Return the updated price
        return JsonResponse({'updated_price': formatted_price})

    # Render the product detail template
    return render(request, 'products/product_detail.html', {
        'product': product,
        'storage_options': storage_options,
        'is_network_required': is_network_required,
        
    
    })


def search_results(request):
    search_query =request.GET.get('search', '')  # Get the search query from the GET request
    products = Product.objects.filter(name__icontains=search_query)  # Case-insensitive search by product name
    
    if request.is_ajax():  # Check if the request is AJAX (for JSON response)
        products_data = [{'slug': product.slug, 'name': product.name} for product in products]
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




