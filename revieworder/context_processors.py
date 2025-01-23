from django.db.models import Sum
from .models import Cart

# Quantity of items in the cart for the navbar
def cart_total_quantity(request):
    total_quantity = 0
    if request.user.is_authenticated:
        total_quantity = Cart.objects.filter(user=request.user).count()
    return {
        'total_quantity': total_quantity
    }
