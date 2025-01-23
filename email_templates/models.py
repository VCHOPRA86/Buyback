# email_templates/models.py
from django.db import models
from django.apps import apps 
from checkout.constants import STATUS_CHOICES



class OrderStatus(models.Model):
    """Model for order statuses."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class EmailTemplate(models.Model):
    order_status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name="Order Status")
    subject = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

    def get_status_display(self):
        """Fetch display name for the status dynamically."""
        Order = apps.get_model('checkout', 'Order')  # Dynamically get the Order model
        for choice_value, choice_label in Order.STATUS_CHOICES:
            if self.order_status == choice_value:
                return choice_label
        return self.order_status  # Fallback to raw value if no match    