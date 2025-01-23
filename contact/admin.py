
# contact_us/admin.py

from django.contrib import admin
from .models import ContactSubmission


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'order_no', 'message', 'get_submitted_at_date')
    search_fields = ('name', 'email')
    readonly_fields = ('name', 'email', 'company', 'order_no', 'phone', 'message', 'submitted_at')

     # Disable the "Add" button
    def has_add_permission(self, request):
        return False
    
    # Disable the "Change" button (edit functionality)
    def has_change_permission(self, request, obj=None):
        return False

     # Custom method to display 'submitted_at' as 'DATE' in the list view
    @admin.display(description='DATE')
    def get_submitted_at_date(self, obj):
        return obj.submitted_at.strftime('%d-%M-%Y %H:%M:%S')  # Customize the date format as needed

