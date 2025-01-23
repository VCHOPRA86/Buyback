from django.db import models
from .constants import STATUS_CHOICES
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from profiles.models import Profile
from products.models import Product
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from email_templates.models import EmailTemplate


class Order(models.Model):

    PAYMENT_CHOICES = [
        ('PayPal', 'PayPal'),
        ('Bank Transfer', 'Bank Transfer'),
    ]

   
    POSTAGE_CHOICES = [
        ('paid_by_sender', 'Postage Paid by Sender'),
        ('prepaid', 'Prepaid Postage'),
    ]


    order_number = models.CharField(max_length=32, null=False, editable=False, blank=True) 
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    postage_option = models.CharField(max_length=20, choices=POSTAGE_CHOICES, default='')
    prepaid_label_url = models.URLField(blank=True, null=True)  # Stores the label download URL
    tracking_code = models.CharField(max_length=50, blank=True, null=True)  # Stores the tracking code
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    contact_number = models.CharField(max_length=20, null=False, blank=False)
    address = models.TextField(max_length=80, null=False, blank=False)
    address_line_2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=80, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, null=False, blank=False)
    account_name = models.CharField(max_length=50, null=False, blank=False)
    account_number = models.CharField(max_length=20, null=False, blank=False)
    sort_code = models.CharField(max_length=20, null=False, blank=False)
    paypal_email = models.EmailField(max_length=254, null=False, blank=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    revised_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    revised_reason = models.TextField(null=True, blank=True)  # Reason for price revision
    user_response = models.CharField(
        max_length=10,
        choices=[
            ('Accepted', 'Accepted'),
            ('Rejected', 'Rejected'),
            ('Pending', 'Pending')
        ],
        null=True, blank=True
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Awaiting Delivery')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    

    

    class Meta:
        verbose_name = "Your Order"
        verbose_name_plural = "Your Orders"

    def generate_order_number(self):
        """Generate a unique order number."""
        return f"CTG{self.id:06d}"

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new and not self.order_number:
            self.order_number = self.generate_order_number()
            super().save(update_fields=['order_number'])

    def __str__(self):
        return f"Order #{self.order_number} - {self.payment_method} - {self.status}"    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orderitems", null=True) 
    quantity = models.PositiveIntegerField(default=1)
    product_name = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    network = models.CharField(max_length=255, blank=True, null=True)
    storage_size = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        if self.product:
            return f"{self.product.name} {self.storage_size or ''} {self.network or ''} ({self.condition or ''})"
        return f"{self.product_name or 'Unknown Product'} {self.storage_size or ''} {self.network or ''} ({self.condition or ''})"

