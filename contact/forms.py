# contact/forms.py

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    company = forms.CharField(max_length=100, required=False)
    order_no = forms.CharField(max_length=100, required=False)
    phone = forms.CharField(max_length=15, required=False)
    message = forms.CharField(widget=forms.Textarea, required=True)

