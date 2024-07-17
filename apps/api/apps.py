from django.apps import AppConfig


MAJOR_VERSION = 1
MINOR_VERSION = 0
PATCH_VERSION = 0


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.api'
