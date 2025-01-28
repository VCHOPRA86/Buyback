from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.shortcuts import redirect
from .models import GlobalSettings

@admin.register(GlobalSettings)
class GlobalSettingsAdmin(admin.ModelAdmin):
    list_display = ('maintenance_mode_status', 'maintenance_message', 'toggle_maintenance_mode', 
                    'toggle_prepaid_postage_label', 'toggle_paid_by_sender')
    list_display_links = ('maintenance_message',)

    def maintenance_mode_status(self, obj):
        """Display current maintenance mode status."""
        return "ON" if obj.maintenance_mode else "OFF"
    maintenance_mode_status.short_description = "Maintenance Mode Status"

    def toggle_maintenance_mode(self, obj):
        """Provide a toggle button for maintenance mode."""
        if obj.maintenance_mode:
            toggle_url = reverse('admin:toggle_maintenance_mode', args=[obj.id, 'off'])
            button_color = "red"
            label = "Turn OFF"
        else:
            toggle_url = reverse('admin:toggle_maintenance_mode', args=[obj.id, 'on'])
            button_color = "green"
            label = "Turn ON"

        return format_html(
            '<a href="{}" style="color: white; background-color: {}; padding: 5px 10px; border-radius: 5px; text-decoration: none;">{}</a>',
            toggle_url,
            button_color,
            label
        )
    toggle_maintenance_mode.short_description = "Toggle Maintenance Mode"

    def toggle_prepaid_postage_label(self, obj):
        """Provide a toggle button for the prepaid postage label option."""
        if obj.prepaid_postage_label_enabled:
            toggle_url = reverse('admin:toggle_prepaid_postage_label', args=[obj.id, 'disable'])
            button_color = "red"
            label = "Disable Prepaid Label"
        else:
            toggle_url = reverse('admin:toggle_prepaid_postage_label', args=[obj.id, 'enable'])
            button_color = "green"
            label = "Enable Prepaid Label"

        return format_html(
            '<a href="{}" style="color: white; background-color: {}; padding: 5px 10px; border-radius: 5px; text-decoration: none;">{}</a>',
            toggle_url,
            button_color,
            label
        )
    toggle_prepaid_postage_label.short_description = "Toggle Prepaid Postage Label"

    def toggle_paid_by_sender(self, obj):
        """Provide a toggle button for Paid by Sender option."""
        if obj.paid_by_sender_enabled:
            toggle_url = reverse('admin:toggle_paid_by_sender', args=[obj.id, 'disable'])
            button_color = "red"
            label = "Disable Paid by Sender"
        else:
            toggle_url = reverse('admin:toggle_paid_by_sender', args=[obj.id, 'enable'])
            button_color = "green"
            label = "Enable Paid by Sender"

        return format_html(
            '<a href="{}" style="color: white; background-color: {}; padding: 5px 10px; border-radius: 5px; text-decoration: none;">{}</a>',
            toggle_url,
            button_color,
            label
        )
    toggle_paid_by_sender.short_description = "Toggle Paid by Sender"

    def get_urls(self):
        """Add a custom URL to handle toggling."""
        from django.urls import path
        custom_urls = [
            path(
                '<int:pk>/toggle/maintenance/<str:action>/',
                self.admin_site.admin_view(self.toggle_maintenance_view),
                name='toggle_maintenance_mode',
            ),
            path(
                '<int:pk>/toggle/prepaid_postage_label/<str:action>/',
                self.admin_site.admin_view(self.toggle_prepaid_postage_label_view),
                name='toggle_prepaid_postage_label',  # Ensure this matches the URL pattern
            ),
            path(
                '<int:pk>/toggle/paid_by_sender/<str:action>/',
                self.admin_site.admin_view(self.toggle_paid_by_sender_view),
                name='toggle_paid_by_sender',  # Ensure this matches the URL pattern
            ),
        ]
        return custom_urls + super().get_urls()

    def toggle_maintenance_view(self, request, pk, action):
        """Handle maintenance mode toggling."""
        obj = GlobalSettings.objects.get(pk=pk)
        if action == "on":
            obj.maintenance_mode = True
        elif action == "off":
            obj.maintenance_mode = False

        obj.save()
        self.message_user(request, f"Maintenance mode turned {'ON' if obj.maintenance_mode else 'OFF'}.")
        return redirect('admin:settings_globalsettings_changelist')

    def toggle_prepaid_postage_label_view(self, request, pk, action):
        """Handle prepaid postage label feature toggling."""
        obj = GlobalSettings.objects.get(pk=pk)
        obj.prepaid_postage_label_enabled = True if action == "enable" else False
        obj.save()
        self.message_user(request, f"Prepaid postage label feature {'enabled' if obj.prepaid_postage_label_enabled else 'disabled'}.")
        return redirect('admin:settings_globalsettings_changelist')

    def toggle_paid_by_sender_view(self, request, pk, action):
        """Handle Paid by Sender feature toggling."""
        obj = GlobalSettings.objects.get(pk=pk)
        obj.paid_by_sender_enabled = True if action == "enable" else False
        obj.save()
        self.message_user(request, f"Paid by Sender feature {'enabled' if obj.paid_by_sender_enabled else 'disabled'}.")
        return redirect('admin:settings_globalsettings_changelist')
