from django.apps import AppConfig


class RevieworderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'revieworder'

    def ready(self):
        import revieworder.signals
