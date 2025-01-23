from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from .models import Order, OrderItem
from django.utils.html import format_html


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # make country not a required field
        self.fields['country'].required = False
        

        
        payment_method = self.initial.get("payment_method", "").lower()

        # Dynamically make fields required based on the selected payment method
        if payment_method == "paypal":
            self.fields['paypal_email'].required = True
            self.fields['account_name'].required = False
            self.fields['account_number'].required = False
            self.fields['sort_code'].required = False
        elif payment_method == "bank transfer":
            self.fields['account_name'].required = True
            self.fields['account_number'].required = True
            self.fields['sort_code'].required = True
            self.fields['paypal_email'].required = False
        else:
            self.fields['paypal_email'].required = False
            self.fields['account_name'].required = False
            self.fields['account_number'].required = False
            self.fields['sort_code'].required = False

    def clean(self):
        cleaned_data = super().clean()
        payment_method = cleaned_data.get("payment_method", "").lower()
        paypal_email = cleaned_data.get("paypal_email")
        account_name = cleaned_data.get("account_name")
        account_number = cleaned_data.get("account_number")
        sort_code = cleaned_data.get("sort_code")
  

        if payment_method == "paypal" and not paypal_email:
            raise ValidationError("PayPal email is required when the payment method is PayPal.")

        if payment_method == "bank transfer":
            if not all([account_name, account_number, sort_code]):
                raise ValidationError("Account name, account number, and sort code are required for bank transfer.")

        # If neither payment method is properly filled, raise an error
        if payment_method not in ["paypal", "bank transfer"]:
            raise ValidationError("Invalid payment method. Choose either PayPal or Bank Transfer.")
        

        return cleaned_data

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    fields = ['product_details', 'quantity', 'value']
    readonly_fields = ['product_details', 'quantity', 'value']

    def product_details(self, obj):
        if obj.product:
            product_name = obj.product.name or "Unknown Product"
            storage = obj.storage_size or "Unknown Storage"
            network = obj.network or "Unknown Network"
            condition = obj.condition or "Unknown Condition"
            return format_html(
                "{} {} {} ({})",
                product_name,
                storage,
                network,
                condition
            )
        elif obj.product_name:
            return format_html(
                "{} {} {} ({})",
                obj.product_name,
                obj.storage_size or "Unknown Storage",
                obj.network or "Unknown Network",
                obj.condition or "Unknown Condition"
            )
        return format_html('<span style="color:red;">No Product Details Available</span>')

    product_details.short_description = 'Product Details'


class OrderAdmin(admin.ModelAdmin):
    form = OrderForm  # Use the custom form
    inlines = [OrderItemInline]

    list_display = (
        'order_number', 'payment_details', 'total_trade_in',
        'total_price', 'status', 'formatted_created_at'
    )
    search_fields = ('order_number', 'payment_method', 'status')
    list_filter = ('status', 'created_at', 'payment_method')
    ordering = ('-created_at',)

    def payment_details(self, obj):
        if not obj.payment_method:
            return "N/A"
        if obj.payment_method.lower() == "paypal" and obj.paypal_email:
            return f"PayPal Email: {obj.paypal_email}"
        elif obj.payment_method.lower() == "bank transfer" and all(
            [obj.account_name, obj.account_number, obj.sort_code]
        ):
            return (
                f"Account Name: {obj.account_name}, "
                f"Account Number: {obj.account_number}, "
                f"Sort Code: {obj.sort_code}"
            )
        return "Incomplete Payment Details"

    payment_details.short_description = "Payment Details"

    def total_trade_in(self, obj):
        if not obj.profile:
            return "N/A"
        profile = obj.profile
        order_count = Order.objects.filter(profile=profile).count()
        return format_html(
            '<a href="/admin/profiles/profile/{}/change/">{}</a>',
            profile.id,
            order_count
        )

    total_trade_in.short_description = "Total Trade-In"

    def formatted_created_at(self, obj):
        return obj.created_at.strftime('%d/%m/%y %I:%M%p').lower()

    formatted_created_at.short_description = 'Created At'

    class Media:
        js = ('js/admin/collapse_filters.js',)
        css = {
            'all': ('css/admin/admin.css',)
        }


# Register the models with their custom admin classes
admin.site.register(Order, OrderAdmin)
