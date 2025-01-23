from django.contrib import admin, messages
from django.urls import path
from django.http import JsonResponse
from django.utils.html import format_html
from .models import Category, Brand, Product, StorageOption
from decimal import Decimal


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'category')
    search_fields = ('name',)
    actions = ['custom_delete_action']


    def custom_delete_action(self, request, queryset):
        deletable_brands = []
        non_deletable_brands = []

        for brand in queryset:
            if Product.objects.filter(brand=brand).exists():
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
                f"Cannot delete the following brands because they are linked to active products: "
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
        if obj.Product_set.exists():
            # If the brand is linked to a category, prevent deletion
            self.message_user(
                request, 
                "Cannot delete brand because it is linked to one or more products.", 
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

    list_display = ('name', 'brand', 'category', 'formatted_working_price', 'formatted_faulty_price')
    exclude = ('price',)  # Excludes 'price' field
    fields = ('category', 'brand', 'image', 'name', 'description', 'working_price', 'faulty_price', 'working_description', 'faulty_description', 'unlocked_price_adjustment', 'ee_price_adjustment', 'o2_price_adjustment', 'vodafone_price_adjustment', 'three_price_adjustment', 'storage_options')
    search_fields = ('name', 'brand__name', 'category__name')  # Make searching by brand or by categories easier
    filter_horizontal = ("storage_options",)  # Add a multi-select widget for storage options
    
    

    def get_inline_instances(self, request, obj=None):
        """
        Only show storage options inline if the category is Phones or Tablets.
        """
        if obj and obj.category.name in ['Phones', 'Tablets']:
            return super().get_inline_instances(request, obj)
        return []

    
    
    class Media:
        js = 'js/admin/dynamic_brand_filter.js',
        css = {'all': ('css/admin/admin.css',)}


    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
        path('filter_brands/', self.admin_site.admin_view(self.filter_brands), name='filter_brands'),
            ]
        return custom_urls + urls

    def filter_brands(self, request):
        category_id = request.GET.get('category_id')
        brands = Brand.objects.filter(category_id=category_id).values('id', 'name')
        return JsonResponse({'brands': list(brands)})



    def formatted_working_price(self, obj):
        # Safely return the working price with a "+" sign
        return format_html('<span style="color:green">+£{}</span>', obj.working_price)
    formatted_working_price.short_description = 'Working Price (+)'

    def formatted_faulty_price(self, obj):
        # Safely return the faulty price with a "-" sign
        return format_html('<span style="color:red">-£{}</span>', obj.faulty_price)
    formatted_faulty_price.short_description = 'Faulty Price (-)'
    
    def changelist_view(self, request, extra_context=None):
        # Add a helpful message when the product list page is accessed
        if not request.GET.get('q'):  # Display message if there's no search query
            messages.info(request, "Products can be searched by brand or category. Use the search bar to filter products easily.")
        return super().changelist_view(request, extra_context)
    

    def save_model(self, request, obj, form, change):
        # Ensure that working_price defaults to 0.00 if not set
        if not obj.working_price:
            obj.working_price = Decimal('0.00')  # Default to 0.00 if not set
        
        # Ensure that faulty_price defaults to 0.00 if not set
        if not obj.faulty_price:
            obj.faulty_price = Decimal('0.00')  # Default to 0.00 if not set

        super().save_model(request, obj, form, change)
        

      

@admin.register(StorageOption)
class StorageOptionAdmin(admin.ModelAdmin):
    list_display = ("size", "formatted_additional_price")  # Use formatted_additional_price instead of additional_price
    search_fields = ("size",)
    ordering = ("additional_price",)  # Order by additional_price in ascending order  

    def formatted_additional_price(self, obj):
        # Safely return the additional price with a "+" sign
        return format_html('<span style="color:green">+£{}</span>', obj.additional_price)

    # Give a friendly name for the column
    formatted_additional_price.short_description = 'Additional Price'