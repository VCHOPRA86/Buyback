import logging
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from checkout.models import Order, OrderItem
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from .models import Cart
from products.models import Product
from django.db.models import Sum

logger = logging.getLogger(__name__)


def add_to_cart(request, product_slug):
    if request.method == "POST":
        # Fetch the product using the slug
        product = get_object_or_404(Product, slug=product_slug)

        product_name = request.POST.get('product_name')
        condition = request.POST.get('condition')
        network = request.POST.get('network')
        value = request.POST.get('price')
        storage_size = request.POST.get('storage_size')

        print(f"Product: {product_name}, Condition: {condition}, Network: {network}, Price: {value}, Storage: {storage_size}")

        # Validate product type
        if product.category.name.lower() in ['phones', 'tablets'] and not network:
            messages.error(request, "Network is required for phones and tablets.")
            return redirect('product_detail', product_slug=product_slug)

        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Save to the database if the user is logged in
            Cart.objects.create(
                user=request.user,
                product_name=product_name,
                condition=condition,
                network=network,
                value=value,
                storage_size=storage_size,
            )

            # Update session cart count
            cart_count = Cart.objects.filter(user=request.user).count()
            request.session['cart_count'] = cart_count
            return redirect('revieworder:revieworder')
        else:
            # Save the cart item to the session for unauthenticated users
            cart_item = {
                'product_name': product_name,
                'condition': condition,
                'network': network,
                'value': value,
                'storage_size': storage_size,
            }
            cart = request.session.get('cart', [])
            cart.append(cart_item)
            request.session['cart'] = cart
            request.session.modified = True  # Mark the session as modified to save changes

        # Redirect to login with 'next' parameter to go back to cart page after login
            login_url = f"{reverse('account_login')}?next={reverse('revieworder:revieworder')}"
            return redirect(f'{login_url}?next={request.path}')
        

    return redirect('product_detail', product_slug=product_slug)



def remove_from_cart(request, item_id):
    try:
        cart_item = Cart.objects.get(id=item_id, user=request.user)
        cart_item.delete()

        # Recalculate cart count and total
        cart_count = Cart.objects.filter(user=request.user).count()
        cart_total = Cart.objects.filter(user=request.user).aggregate(total=Sum('value'))['total'] or 0

        # Update session
        request.session['cart_count'] = cart_count
        request.session['cart_total'] = float(cart_total)

        return JsonResponse({
            'success': True,
            'cart_total': cart_total,
            'cart_count': cart_count,
            'message': 'Item removed successfully',
        })
    except Cart.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'Item not found in cart',
        })

@login_required
def revieworder(request):
    cart_items = Cart.objects.filter(user=request.user).order_by('-added_on')

    for item in cart_items:
        item.network = item.network or ""

    cart_total = sum(item.value for item in cart_items)

    # Get the product slug from the first item in the cart (assuming all items share the same product slug)
    product_slug = None
    if cart_items:
        product = Product.objects.filter(name=cart_items[0].product_name).first()
        product_slug = product.slug if product else None


    # Update session for display purposes
    request.session['cart_count'] = cart_items.count()
    request.session['cart_total'] = float(cart_total)

    return render(request, 'revieworder/revieworder.html', {
        'cart_items': cart_items,
        'cart_total': cart_total,
        'product_slug': None  # Adjust as necessary
    })


def review_sale(request):
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        account_name = request.POST.get('account_name', '').strip()
        account_number = request.POST.get('account_number', '').strip()
        sort_code = "-".join([
            request.POST.get(f'sort_code_{i}', '').strip() for i in range(1, 4)
        ])
        paypal_email = request.POST.get('paypal_email', '').strip()

        cart_items = Cart.objects.filter(user=request.user)
        cart_total = sum(item.value for item in cart_items)

        request.session['payment_details'] = {
            'payment_method': payment_method,
            'account_name': account_name,
            'account_number': account_number,
            'sort_code': sort_code,
            'paypal_email': paypal_email,
        }

        request.session['cart_items'] = [
            {
                'product_name': item.product_name,
                'condition': item.condition,
                'value': float(item.value),
                'network': item.network,
                'storage_size': item.storage_size,
            }
            for item in cart_items
        ]
        request.session['cart_total'] = float(cart_total)

        request.session.save()

        return redirect('checkout')

    return redirect('revieworder')


