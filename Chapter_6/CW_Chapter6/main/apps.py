import os

from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        if os.environ.get('RUN_MAIN') == 'True':
            from main.services import start_scheduler
            start_scheduler()

