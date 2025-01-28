from django.shortcuts import render
from .models import GlobalSettings
from django.urls import reverse

class SettingsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            global_settings = GlobalSettings.objects.first()
            if global_settings and global_settings.maintenance_mode:
                # Bypass maintenance mode for admin paths or superusers
                if request.path.startswith(reverse('admin:index')) or request.user.is_superuser:
                    return self.get_response(request)   
                
                # Show maintenance page
                return render(request, 'settings/maintenance.html', {
                    'message': global_settings.maintenance_message,
                })
        except GlobalSettings.DoesNotExist:
            pass

        return self.get_response(request)
