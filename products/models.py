from django.db import models
from ckeditor.fields import RichTextField
from decimal import Decimal
from django.utils.text import slugify


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # Automatically generate a slug from the category name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True, help_text="A URL-friendly version of the brand name, used for linking to the brand's page.")
    image = models.ImageField(upload_to='brands/', null=True, blank=True)
    description = models.TextField(blank=True, null=True)  
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # Auto-generate the slug from the name field
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    


class ModelType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# Define StorageOption first
class StorageOption(models.Model):
    size = models.CharField(max_length=50)  # Example: '256GB', '512GB'
    additional_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    
    

    def __str__(self):
        return f"{self.size} (+£{self.additional_price})" 


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name="products", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    working_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), null=True, blank=True)
    faulty_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), null=True, blank=True)

    storage_options = models.ManyToManyField(StorageOption, related_name="products", blank=True)
    # New fields for specific descriptions
    working_description = RichTextField(blank=True, null=True, help_text='Description for working condition - Use <code>class="no-bullets"</code> in your <ul> tags to remove bullet points')
    faulty_description =  RichTextField(blank=True, null=True, help_text='Description for faulty condition - Use <code>class="no-bullets"</code> in your <ul> tags to remove bullet points' )

    # New fields for network status price adjustments
    unlocked_price_adjustment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    ee_price_adjustment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    o2_price_adjustment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    vodafone_price_adjustment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    three_price_adjustment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    # Add additional network statuses as needed

    def save(self, *args, **kwargs):
        # Automatically generate the slug if not provided
        if not self.slug:  
            base_slug = slugify(self.name)  # Create a slug from the product name
            slug = base_slug
            counter = 1
            # Ensure the slug is unique by checking the database for any existing products with the same slug
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        
        # Call the parent class's save method to save the product
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
        
    def get_price_by_condition_and_network(self, condition, network_status, storage_size=None):
        """
        Calculate price based on the selected condition, network status, and storage size.
        """
        # Set the base_price according to the condition directly
        base_price = Decimal(self.faulty_price if condition == 'faulty' else self.working_price)

        # Apply network price adjustments directly to the base_price
        if network_status == 'unlocked':
            base_price += Decimal(self.unlocked_price_adjustment or 0)
        elif network_status == 'ee':
            base_price += Decimal(self.ee_price_adjustment or 0)
        elif network_status == 'o2':
            base_price += Decimal(self.o2_price_adjustment or 0)
        elif network_status == 'vodafone':
            base_price += Decimal(self.vodafone_price_adjustment or 0)
        elif network_status == 'three':
            base_price += Decimal(self.three_price_adjustment or 0)

        # Apply storage price adjustment if a storage size is specified
        if storage_size:
            storage_option = self.storage_options.filter(size=storage_size).first()
            if storage_option:
                base_price += Decimal(storage_option.additional_price or 0)

        # Return the calculated price
        return base_price
    
  
    