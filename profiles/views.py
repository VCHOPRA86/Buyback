from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.core.mail import send_mail
from checkout.models import Order
from django.contrib.auth.decorators import login_required
from .forms import ProfileEditForm, UserEditForm
from .models import Profile
from django.contrib import messages
from django.conf import settings
from email_templates.models import EmailTemplate

@login_required
def profile(request):
    # Get all orders for the logged-in user, ordered by order date
    orders = Order.objects.filter(profile=request.user.profile).order_by('-date')

    if request.method == "POST":
        order_id = request.POST.get('order_id')
        response = request.POST.get('response')
        if order_id and response in ['Accepted', 'Rejected']:
            order = get_object_or_404(Order, id=order_id, profile=request.user.profile)
            order.user_response = response
            order.save()

            # Prepare a string with order item details
            order_items = order.items.all()  # Get all items related to this order
            item_details = "\n".join([f"Product: {item.product_name}, Quantity: {item.quantity}, Value: {item.value}" 
                                      for item in order_items])

            # Send an email to the admin when the user accepts or rejects the offer
            if response == 'Accepted':
                subject = 'Order Accepted'
                message = f'The user {order.profile.user.username} has accepted your offer for order {order.order_number}.\n\n' \
                          f"Order Items:\n{item_details}\n" \
                          f"Revised Price:{order.revised_price}"
                
                # Send email to admin, using the admin email from settings.py
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL])
            elif response == 'Rejected':
                subject = 'Order Rejected'
                message = f'The user {order.profile.user.username} has rejected your offer for order {order.order_number}.\n\n' \
                          f"Order Items:\n{item_details}\n" \
                          f"Revised Price:{order.revised_price}"
                # Send email to admin, using the admin email from settings.py
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL])

               # Fetch the email template based on the order response (Accepted/Rejected)
            email_template = EmailTemplate.objects.filter(order_status=response).first()
            if email_template:
                subject = email_template.subject
                body = email_template.body

                # Replace placeholders in the body with actual data
                body = body.replace("{{user_name}}", order.profile.user.username)
                body = body.replace("{{order_number}}", order.order_number)
                body = body.replace("{{item_details}}", item_details)
                body = body.replace("{{revised_price}}", str(order.revised_price))

                # Send email to the customer (the user who placed the order)
                send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [order.profile.user.email])


    # Setup pagination
    paginator = Paginator(orders, 10)  # Show 10 orders per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'profiles/profile.html', {'page_obj': page_obj})
@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            # Add a success message after saving the forms
            messages.success(request, 'Your profile has been updated successfully!')

            # Debugging: Print updated data to ensure it's saved
            print(f"Updated User: {request.user.first_name} {request.user.last_name}, Email: {request.user.email}")
            print(f"Profile: {profile.address}, {profile.address_line2}, {profile.city}")

            return redirect('profile')  # Redirect to the user's profile page
        else:
            # Add an error message if the forms are invalid
            messages.error(request, 'There was an error updating your profile. Please try again.')

            # Debugging: Print errors if forms are invalid
            print("User Form Errors:", user_form.errors)
            print("Profile Form Errors:", profile_form.errors)
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=profile)

    return render(request, 'profiles/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})


def profile_orders(request, id):
    # Fetch the order with the given ID
    order = get_object_or_404(Order, id=id)
    # Render the order details template with the order data
    return render(request, 'profiles/print_orders.html', {'order': order})




