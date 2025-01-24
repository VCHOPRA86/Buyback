from .models import Cart

def cart_total_quantity(request):
    total_quantity = 0
    
    # For authenticated users
    if request.user.is_authenticated:
        total_quantity = Cart.objects.filter(user=request.user).count()
    
    # For unauthenticated users (checking the session)
    elif 'cart' in request.session:
        total_quantity = len(request.session['cart'])

    return {
        'total_quantity': total_quantity
    }
