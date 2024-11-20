from django.contrib import admin, messages
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
    actions = ['custom_delete_action']


    def custom_delete_action(self, request, queryset):
        deletable_brands = []
        non_deletable_brands = []

        for brand in queryset:
            if Category.objects.filter(brand=brand).exists() or Product.objects.filter(brand=brand).exists():
                non_deletable_brands.append(brand)
            else:
                deletable_brands.append(brand)

        if deletable_brands:
            for brand in deletable_brands:
                brand.delete()
            self.message_user(
                request, 
                f"Successfully deleted {len(deletable_brands)} brand(s).",
                level=messages.SUCCESS
            )
        if non_deletable_brands:
            self.message_user(
                request,
                f"Cannot delete the following brands because they are linked to active categories or products: "
                f"{', '.join([brand.name for brand in non_deletable_brands])}.",
                level=messages.WARNING
            )


    custom_delete_action.short_description = "Delete Selected Brands"

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def delete_model(self, request, obj):
        # Check if the brand is linked to any categories
        if obj.category:
            # If the brand is linked to a category, prevent deletion
            self.message_user(
                request, 
                "Cannot delete brand because it is linked to one or more categories.", 
                level=messages.WARNING
            )
        else:
            # Proceed with deletion if the brand is not linked to a category
            super().delete_model(request, obj)
            self.message_user(request, "Brand deleted successfully.", level=messages.SUCCESS)
            
    def message_user(self, request, message, level=messages.INFO, extra_tags='', fail_silently=False):
        # Suppress the automatic "deleted successfully" message
        if "deleted successfully" not in message:
            super().message_user(request, message, level, extra_tags, fail_silently)


    

    def has_delete_permission(self, request, obj=None):
        if obj and request.user.has_perm('products.delete_brand'):
            return True
        return False
        

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
    
    