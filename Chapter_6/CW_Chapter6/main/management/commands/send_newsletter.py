
from django.core.management import BaseCommand
from main.cron import send_newsletter_periodic_email


class Command(BaseCommand):
    def handle(self, *args, **options):
        send_newsletter_periodic_email()
