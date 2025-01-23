from django.db.models.signals import post_save
from allauth.account.signals import user_signed_up
from django.core.mail import send_mail
from django.dispatch import receiver
from .models import Profile
from django.conf import settings
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(user_signed_up)
def send_welcome_email(sender, request, user, **kwargs):
    logger.debug(f"Sending welcome email to {user.email}")  # Log to verify if function is called
    print(f"Sending welcome email to: {user.email}")  # Debug in console

    subject = "Welcome to CashThatGadgets!"
    message = f"Hello {user.username},\n.\n\nThank you for signing up with CashThatGadgets. We're excited to have you on board!\n\nBest regards,\nThe CashThatGadgets Team"
    recipient = [user.email]  # Send to the user's email

    try:
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")