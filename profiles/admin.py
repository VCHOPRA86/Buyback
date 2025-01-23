from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.db import transaction
from .models import Profile
from .forms import ProfileAdminForm  # Import your form

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm
    list_display = (
        'user', 
        'first_name', 
        'last_name', 
        'email', 
        'contact_number', 
        'date_joined', 
        'edit_link', 
        'delete_link'
    )
    actions = ['deactivate_users', 'activate_users']

    def deactivate_users(self, request, queryset):
        """Action to deactivate selected users"""
        with transaction.atomic():
            for profile in queryset:
                user = profile.user
                user.is_active = False  # Set is_active to False on the User model
                user.save()

    deactivate_users.short_description = "Deactivate Customer Account"

    def activate_users(self, request, queryset):
        """Action to activate selected users"""
        with transaction.atomic():
            for profile in queryset:
                user = profile.user
                user.is_active = True  # Set is_active to True on the User model
                user.save()

    activate_users.short_description = "Reactivate Customer Account"


    # Display related User fields
    def first_name(self, obj):
        return obj.user.first_name
    first_name.admin_order_field = 'user__first_name'
    first_name.short_description = 'First Name'

    def last_name(self, obj):
        return obj.user.last_name
    last_name.admin_order_field = 'user__last_name'
    last_name.short_description = 'Last Name'

    def email(self, obj):
        return obj.user.email
    email.admin_order_field = 'user__email'
    email.short_description = 'Email'


    def date_joined(self, obj):
        return obj.user.date_joined  # Access date_joined from the related user
    
    def edit_link(self, obj):
        # Generate the URL for the edit page
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        return format_html('<a href="{}">Edit</a>', url)
    
    def delete_link(self, obj):
        # Generate the URL for the delete confirmation page
        url = reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        return format_html('<a href="{}">Delete</a>', url)
    
    def delete_model(self, request, obj):
        with transaction.atomic():
            # Delete the related user
            obj.user.delete()
            # Delete the profile
            obj.delete()

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        print(f"Profile saved in admin: {obj}")

    def get_queryset(self, request):
        # Exclude admin and staff users from queryset
        queryset = super().get_queryset(request)
        return queryset.filter(user__is_staff=False)  # Filter out staff/admin accounts
            

    # Optional: Set ordering or short description for admin display
    email.admin_order_field = 'user__email'
    email.short_description = 'Email Address'
    date_joined.admin_order_field = 'user__date_joined'
    date_joined.short_description = 'Date Joined'
