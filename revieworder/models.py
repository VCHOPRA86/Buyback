from django.db import models
from django.contrib.auth.models import User
from products.models import Product  # Ensure this import points to your Product model

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    product_name = models.CharField(max_length=255, default="Unknown Product")
    condition = models.CharField(max_length=50, default='working')
    network = models.CharField(max_length=50, null=True, blank=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)
    storage_size = models.CharField(max_length=50, default="128GB")  # Add storage_size field



    def __str__(self):
        return f"{self.user.username} - {self.product_name} - {self.condition} - {self.network} - {self.storage_size} - £{self.value} - {self.quantity}"
    
