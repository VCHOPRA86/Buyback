# email_templates/admin.py
from django.contrib import admin
from .models import EmailTemplate


class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ('order_status', 'subject', 'created_at', 'updated_at')
    search_fields = ('order_status__name', 'subject')

 

admin.site.register(EmailTemplate, EmailTemplateAdmin)
