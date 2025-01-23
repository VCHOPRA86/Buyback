from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", unique=True) # Use related_name="profile"# Add related_name here
    is_active = models.BooleanField(default=True) 
    contact_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True)
    county = models.CharField(max_length=100, blank=True)
    post_code = models.CharField(max_length=10, blank=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Customer Accounts"
        verbose_name_plural = "Cutomer Accounts"
    

    def __str__(self):
        return f'{self.user.username} Profile'
