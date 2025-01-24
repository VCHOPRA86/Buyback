from allauth.account.signals import user_logged_in
from django.dispatch import receiver
from .models import Cart

@receiver(user_logged_in)
def merge_cart_after_login(sender, request, user, **kwargs):
    # Retrieve session cart
    session_cart = request.session.pop('cart', [])
    if not session_cart:
        print("No cart items in session at login.")
        return

    # Debugging: Log session cart contents
    print(f"Merging session cart for user {user}: {session_cart}")

    # Add session cart items to the database
    for item in session_cart:
        Cart.objects.create(
            user=user,
            product_name=item['product_name'],
            condition=item['condition'],
            network=item['network'],
            value=item['value'],
            storage_size=item['storage_size'],
        )

    # Update session cart count
    request.session['cart_count'] = Cart.objects.filter(user=user).count()
    print(f"Cart merged successfully for user {user}.")
