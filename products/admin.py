from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Brand, Product
from decimal import Decimal


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'brand', 'category', 'formatted_working_price', 'formatted_faulty_price', 'unlocked_price_adjustment', 'ee_price_adjustment')
    exclude = ('price',)  # Excludes 'price' field
    fields = ('category', 'brand', 'image', 'name', 'description', 'working_price', 'faulty_price', 'working_description', 'faulty_description', 'unlocked_price_adjustment', 'ee_price_adjustment')
    search_fields = ('name', 'brand__name')  # Make searching by brand easier
    
    class Media:
        # Reference the custom CSS file
        css = {
            'all': ('css/admin/admin.css',)
        }

        js = ('js/admin/js/custom_ckeditor_config.js',)

    def formatted_working_price(self, obj):
        # Safely return the working price with a "+" sign
        return format_html('<span style="color:green">+£{}</span>', obj.working_price)
    formatted_working_price.short_description = 'Working Price (+)'

    def formatted_faulty_price(self, obj):
        # Safely return the faulty price with a "-" sign
        return format_html('<span style="color:red">-£{}</span>', obj.faulty_price)
    formatted_faulty_price.short_description = 'Faulty Price (-)'

    def save_model(self, request, obj, form, change):
        # Ensure that working_price defaults to 0.00 if not set
        if not obj.working_price:
            obj.working_price = Decimal('0.00')  # Default to 0.00 if not set
        
        # Ensure that faulty_price defaults to 0.00 if not set
        if not obj.faulty_price:
            obj.faulty_price = Decimal('0.00')  # Default to 0.00 if not set

        super().save_model(request, obj, form, change)
    
    