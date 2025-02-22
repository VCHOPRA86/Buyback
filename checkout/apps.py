from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'
    verbose_name = "Orders"  # Change the app label here

    def ready(self):
        import checkout.signals  # Ensure the signals are loaded
