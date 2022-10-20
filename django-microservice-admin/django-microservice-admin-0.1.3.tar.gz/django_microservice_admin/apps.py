from django.db import transaction
from django.apps import AppConfig
from django.conf import settings
import sys


class MicroserviceAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_microservice_admin'

    @transaction.atomic
    def ready(self):

        if 'makemigrations' in sys.argv or 'migrate' in sys.argv:
            return

        from .models import AdminApps

        MICROSERVICE_ADMIN_APP_VARS = ['MICROSERVICE_ADMIN_APP_HOST', 'MICROSERVICE_ADMIN_APP_ORDER']

        for var in MICROSERVICE_ADMIN_APP_VARS:
            if not hasattr(settings, var):
                raise Exception(f"Missing {var} in settings.py")