from django.apps import AppConfig


class AuthoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "autho"

    def ready(self):
        from .signals import handlers # noqa