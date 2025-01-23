from django import forms
from .models import Order

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'phone_number', 'address', 'payment_method', 'bank_account_name', 'bank_account_number', 'sort_code', 'paypal_email']
        widgets = {
            'payment_method': forms.Select(choices=[
                ('Bank Transfer', 'Bank Transfer'),
                ('PayPal', 'PayPal'),
            ])
        }
