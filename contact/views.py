# Create your views here.
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import ContactSubmission
from django.conf import settings
from django.contrib import messages


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        company = request.POST.get('company')
        order_no = request.POST.get('order_no')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Save the submission
        ContactSubmission.objects.create(
            name=name,
            email=email,
            company=company,
            order_no=order_no,
            phone=phone,
            message=message,
        )

        # Send email to admin
        subject = f"New Contact Form Submission from {name}"
        message_content = f"""
        Name: {name}
        Email: {email}
        Company: {company}
        Order No: {order_no}
        Phone: {phone}
        Message: {message}
        """

        admin_email = settings.ADMIN_EMAIL  # Add your admin email here
        send_mail(subject, message_content, settings.DEFAULT_FROM_EMAIL, [admin_email])

        messages.success(request, 'Your message has been successfully sent. We will get back to you soon!')
        return redirect('contact')

    return render(request, 'contact/contact.html')
