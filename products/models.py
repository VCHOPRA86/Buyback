from django.db import models
from ckeditor.fields import RichTextField
from decimal import Decimal

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brands/', null=True, blank=True)
    description = models.TextField(blank=True, null=True)  
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    


class ModelType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name="products", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    working_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), null=True, blank=True)
    faulty_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), null=True, blank=True)

    # New fields for specific descriptions
    working_description = RichTextField(blank=True, null=True, help_text='Description for working condition - Use <code>class="no-bullets"</code> in your <ul> tags to remove bullet points')
    faulty_description =  RichTextField(blank=True, null=True, help_text='Description for faulty condition - Use <code>class="no-bullets"</code> in your <ul> tags to remove bullet points' )

    # New fields for network status price adjustments
    unlocked_price_adjustment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    ee_price_adjustment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    # Add additional network statuses as needed


    def get_price_by_condition_and_network(self, condition, network_status):
        
        """
        Calculate price based on the selected condition and network status.
        """
        # Set the base_price according to the condition directly
        base_price = Decimal(self.faulty_price if condition == 'faulty' else self.working_price)
        
        # Apply network price adjustments directly to the base_price
        if network_status == 'unlocked':
            base_price += Decimal(self.unlocked_price_adjustment or 0)
        elif network_status == 'ee':
            base_price += Decimal(self.ee_price_adjustment or 0)

        # Return the calculated price
        return base_price