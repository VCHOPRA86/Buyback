from django.apps import AppConfig
import importlib

class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "profiles"
    verbose_name = "Customers"  # Change the app label here

    def ready(self):
        importlib.import_module('profiles.signals')