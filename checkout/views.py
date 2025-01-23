from django.shortcuts import render, redirect, get_object_or_404
from settings.models import GlobalSettings 
from django.db import transaction
from email_templates.models import EmailTemplate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
from revieworder.models import Cart
from django.conf import settings
from .models import Order, OrderItem
from profiles.models import Profile
import requests

@login_required
def checkout(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    # Retrieve cart items for the user
    cart_items = Cart.objects.filter(user=user)
    cart_total = sum(item.value for item in cart_items)

    # Retrieve the global settings
    global_settings = GlobalSettings.objects.first()


    # Replace None with an empty string for display purposes
    for item in cart_items:
        item.network = item.network or ""
  

    # Retrieve the payment method and store in session
    if request.method == "POST":
        payment_method = request.POST.get('payment_method')
        request.session[f'payment_method_{user.id}'] = payment_method
        request.session[f'account_name_{user.id}'] = request.POST.get('account_name', '')
        request.session[f'account_number_{user.id}'] = request.POST.get('account_number', '')
        request.session[f'sort_code_{user.id}'] = request.POST.get('sort_code', '')
        request.session[f'paypal_email_{user.id}'] = request.POST.get('paypal_email', '')

    # Store cart items in the session scoped by user
    request.session[f'cart_items_{user.id}'] = [
        {
            'product_name': item.product_name,
            'condition': item.condition,
            'value': float(item.value),
            'network': item.network,
            'storage_size': item.storage_size,
        }
        for item in cart_items
    ]
    request.session[f'cart_total_{user.id}'] = float(cart_total)
    request.session.save()

    context = {
        'profile': profile,
        'cart_items': cart_items,
        'cart_total': cart_total,
        'payment_method': request.session.get(f'payment_method_{user.id}', 'unknown'),
        'full_name': f"{user.first_name} {user.last_name}",
        'settings': global_settings,
    }

    return render(request, 'checkout/checkout.html', context)


def send_order_status_email(order):
    email_template = EmailTemplate.objects.filter(order_status=order.status).first()

    if email_template:
        subject = email_template.subject
        body = email_template.body.format(
            full_name=order.full_name,
            order_number=order.order_number,
            total_price=order.total_price,
        )

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [order.email],
            fail_silently=False,
        )

# Utility function to create a shipment with ShipEngine
def create_shipment_with_shipengine(order, postage_option):
    shipengine_url = "https://api.shipengine.com/v1/labels"
    headers = {
        "Content-Type": "application/json",
        "API-Key": settings.SHIPENGINE_API_KEY,
    }

    # Use your company's address for both ship_from and ship_to
    company_address = {
        "name": "Cash That Gadgets",    
        "address_line1": "123 Main Street",
        "address_line2": "Suite 100",  # Optional
        "city_locality": "New York",
        "state_province": "NY",  # Use a valid two-character state abbreviation
        "postal_code": "10001",  # Replace with your ZIP code
        "country_code": "US",  # Adjust for your country
        "phone": "6546464578",
    }

    payload = {
        "shipment": {
            "carrier_id": "se-223897",
            "service_code": "ups_ground",  # Map to ShipEngine's service codes
            "ship_to": company_address,  # Placeholder address (your company address)
            "ship_from": company_address,  # Your company's actual address
            "packages": [
                {
                    "weight": {
                        "value": 2,  # Package weight in pounds
                        "unit": "pound",
                    },
                    "dimensions": {
                        "length": 10,
                        "width": 6,
                        "height": 4,
                        "unit": "inch",
                    },
                }
            ],
        }, 
        "is_return_label": True,  # Flag for a return label
        "charge_to": {
        "account_number": "123456789",  # Replace with your actual account number
        "method": "on_carrier_acceptance",  # Only charge upon carrier acceptance
    },
}


    try:
        # Make the API call to ShipEngine
        response = requests.post(shipengine_url, json=payload, headers=headers)
        response_data = response.json()

        if response.status_code == 200:
            # Extract and save the label URL to the order
            label_url = response_data["label_download"]["href"]
            tracking_code = response_data["tracking_number"]

            # Save the label URL and tracking code to the order
            order.prepaid_label_url = label_url
            order.tracking_code = tracking_code
            order.save()
            return label_url
        else:
            # Handle ShipEngine error response
            error_message = response_data.get("errors", "Unknown error")
            raise Exception(f"ShipEngine error: {error_message}")

    except requests.RequestException as e:
        # Handle network or other HTTP request-related errors
        raise Exception(f"An error occurred while communicating with ShipEngine: {str(e)}")

@login_required
@transaction.atomic
def confirm_sale(request):
    if request.method == "POST":
        user = request.user

        # Extract postage option from the form
        postage_option = request.POST.get('postage_option')

        # Retrieve order data from session
        payment_method = request.session.get(f'payment_method_{user.id}', 'unknown')
        account_name = request.session.get(f'account_name_{user.id}', '')
        account_number = request.session.get(f'account_number_{user.id}', '')
        sort_code = request.session.get(f'sort_code_{user.id}', '')
        paypal_email = request.session.get(f'paypal_email_{user.id}', '')
        cart_items = request.session.get(f'cart_items_{user.id}', [])
        cart_total = sum(item.get("value", 0) for item in cart_items)

        profile = Profile.objects.get(user=user)

        # Create the order
        order = Order.objects.create(
            profile=profile,
            full_name=f"{user.first_name} {user.last_name}",
            email=user.email,
            contact_number=profile.contact_number,
            address=profile.address,
            address_line_2=profile.address_line2,
            town_or_city=profile.city,
            county=profile.county,
            postcode=profile.post_code,
            payment_method=payment_method,
            account_name=account_name,
            account_number=account_number,
            sort_code=sort_code,
            paypal_email=paypal_email,
            total_price=cart_total,
            postage_option=postage_option,
        )

        # Create OrderItems for each item in the cart
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product_name=item['product_name'],
                condition=item['condition'],
                value=item['value'],
                network=item.get('network', 'N/A'),
                storage_size=item.get('storage_size', 'N/A')
            )
        
        
        # Generate shipping label only if the postage option is "prepaid postage"
        if postage_option == "prepaid":
            try:
                label_url = create_shipment_with_shipengine(order, postage_option)
                order.prepaid_label_url = label_url  # Save the label URL to the order
                messages.success(request, "Shipping label generated successfully.")
                order.save()
            except Exception as e:
                messages.error(request, f"Error generating shipping label: {str(e)}")
          

        # Send order status email
        send_order_status_email(order)

        # Clear session and database cart data
        Cart.objects.filter(user=user).delete()
        for key in [
            f'payment_method_{user.id}', f'account_name_{user.id}', f'account_number_{user.id}',
            f'sort_code_{user.id}', f'paypal_email_{user.id}', f'cart_items_{user.id}',
            f'cart_total_{user.id}'
        ]:
            request.session.pop(key, None)
        request.session.save()

        return redirect("checkout:checkout_success", order_number=order.order_number)

    return redirect('checkout')


@login_required
def checkout_success(request, order_number):
    user = request.user
    order = get_object_or_404(Order, order_number=order_number)

    # Retrieve OrderItems for the order
    order_items = OrderItem.objects.filter(order=order)


    # Calculate the total cart value and total quantity
    cart_total = sum(item.value for item in order_items)
    total_quantity = order_items.count()

    context = {
        'order': order,
        'cart_items': order_items,
        'cart_total': "{:.2f}".format(cart_total),
        'payment_method': order.payment_method,  # Use stored payment method from the order
        'total_quantity': total_quantity,
        'order_number': order_number,
        'label_url': order.prepaid_label_url,  # Pass the label URL to the template
        'tracking_code': order.tracking_code,
    }

    return render(request, 'checkout/checkout_success.html', context)
