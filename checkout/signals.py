from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from email_templates.models import EmailTemplate
from .models import Order

@receiver(post_save, sender=Order)
def send_status_change_email(sender, instance, created, **kwargs):
    # Only send email on status change, not creation
    if not created and instance.status:
        try:
            # Retrieve the corresponding email template
            email_template = EmailTemplate.objects.get(order_status=instance.status)

            # Get the user's email from the profile
            user_email = instance.profile.user.email if instance.profile and instance.profile.user else instance.email

            # Prepare the email subject and body
            subject = email_template.subject
            body = email_template.body.format(
                username=instance.profile.user.username if instance.profile and instance.profile.user else "Customer",
                order_number=instance.order_number,
                status=instance.get_status_display()
            )

            # Send the email
            send_mail(
                subject=subject,
                message=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user_email],
                fail_silently=False,
            )
            print(f"Email sent to {user_email} for order #{instance.order_number} with status {instance.status}")
        except EmailTemplate.DoesNotExist:
            print(f"No email template found for status: {instance.status}")
        except Exception as e:
            print(f"Error sending email: {e}")
