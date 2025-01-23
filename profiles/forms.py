from django import forms as d_forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import User

from .models import Profile
import logging

logger = logging.getLogger(__name__)

# Form used for Admin profile editing
class ProfileAdminForm(d_forms.ModelForm):
    first_name = d_forms.CharField(max_length=150, required=False)
    last_name = d_forms.CharField(max_length=150, required=False)
    email = d_forms.EmailField(required=False)

    class Meta:
        model = Profile
        fields = (
            'user',  # Optional read-only field for clarity
            'first_name',
            'last_name',
            'email',
            'contact_number',
            'address',
            'address_line2',
            'city',
            'county',
            'post_code',
            'company_name',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        profile = super().save(commit=False)
        user = profile.user
        user.first_name = self.cleaned_data.get('first_name', user.first_name)
        user.last_name = self.cleaned_data.get('last_name', user.last_name)
        user.email = self.cleaned_data.get('email', user.email)

        if commit:
            user.save()
            profile.save()
        return profile

class CustomSignupForm(SignupForm):
    # Personal Details
    first_name = d_forms.CharField(
        widget=d_forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = d_forms.CharField(
        widget=d_forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    contact_number = d_forms.CharField(
        widget=d_forms.TextInput(attrs={'placeholder': 'Contact Number'})
    )

    # Address Details
    address = d_forms.CharField(
        widget=d_forms.TextInput(attrs={'placeholder': 'Address'})
    )
    address_line2 = d_forms.CharField(
        required=False,  # Optional field
        widget=d_forms.TextInput(attrs={'placeholder': 'Address Line 2 (Optional)'})
    )
    city = d_forms.CharField(
        widget=d_forms.TextInput(attrs={'placeholder': 'City'})
    )
    county = d_forms.CharField(
        widget=d_forms.TextInput(attrs={'placeholder': 'County'})
    )
    post_code = d_forms.CharField(
        widget=d_forms.TextInput(attrs={'placeholder': 'Post Code'})
    )

    # Email Fields
    email = d_forms.EmailField(
        widget=d_forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    email2 = d_forms.EmailField(
        widget=d_forms.EmailInput(attrs={'placeholder': 'Confirm Email'})
    )

    # Username and Passwords
    username = d_forms.CharField(
        widget=d_forms.TextInput(attrs={'placeholder': 'Username/Email'})
    )
    password1 = d_forms.CharField(
        widget=d_forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    password2 = d_forms.CharField(
        widget=d_forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
    )

    # Optional Company Name
    company_name = d_forms.CharField(
        required=False,  # Optional field
        widget=d_forms.TextInput(attrs={'placeholder': 'Company Name (Optional)'})
    )

    # Terms and Conditions
    agree_to_terms = d_forms.BooleanField(required=True,)


    def save(self, request):
        logger.debug("CustomSignupForm save method called")
        logger.debug(f"Request data: {request.POST}")
        user = super().save(request)
        logger.debug(f"User created with ID: {user.id}")

            # Update User model fields
        user.first_name = self.cleaned_data.get('first_name', '')
        user.last_name = self.cleaned_data.get('last_name', '')
        user.email = self.cleaned_data.get('email', '')
        user.save()


        # Skip profile creation for admin users
        if user.is_staff or user.is_superuser:
            logger.debug(f"Admin user detected. Skipping profile creation for user: {user.id}")
            return user

        try:
            logger.debug("Attempting to create/update profile...")
            Profile.objects.update_or_create(
                user=user,
                defaults={
                    'contact_number': self.cleaned_data.get('contact_number', ''),
                    'address': self.cleaned_data.get('address', ''),
                    'address_line2': self.cleaned_data.get('address_line2', ''),
                    'city': self.cleaned_data.get('city', ''),
                    'county': self.cleaned_data.get('county', ''),
                    'post_code': self.cleaned_data.get('post_code', ''),
                    'company_name': self.cleaned_data.get('company_name', ''),
                }
            )
            logger.debug(f"Profile successfully created/updated for user: {user.id}")
        except Exception as e:
            logger.error(f"Error creating/updating profile for user {user.id}: {e}")
            raise
        return user
    
class ProfileEditForm(d_forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'contact_number', 'address',
            'address_line2', 'city', 'county', 'post_code', 'company_name'
        ]
        widgets = {
            'contact_number': d_forms.TextInput(attrs={'placeholder': 'Contact Number'}),
            'address': d_forms.TextInput(attrs={'placeholder': 'Address'}),
            'address_line2': d_forms.TextInput(attrs={'placeholder': 'Address Line 2'}),
            'city': d_forms.TextInput(attrs={'placeholder': 'City'}),
            'county': d_forms.TextInput(attrs={'placeholder': 'County'}),
            'post_code': d_forms.TextInput(attrs={'placeholder': 'Post Code'}),
            'company_name': d_forms.TextInput(attrs={'placeholder': 'Company Name'}),
        }    

class UserEditForm(d_forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': d_forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': d_forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': d_forms.EmailInput(attrs={'placeholder': 'Email'}),
        }
            

