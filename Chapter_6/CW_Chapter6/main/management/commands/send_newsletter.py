import smtplib
from datetime import datetime, timezone, timedelta

import pytz
from django.conf import settings
from django.core.mail import send_mail
from django.core.management import BaseCommand

from main.models import Newsletter, Message, Log


class Command(BaseCommand):
    """Команда на запуск рассылки"""
    help = 'Send newsletter'

    def handle(self, *args, **options):
        try:
            zone = pytz.timezone(settings.TIME_ZONE)
            current_datetime = datetime.now(zone)

            for newsletter in Newsletter.objects.all():
                if newsletter.end_time < current_datetime:
                    newsletter.status = Newsletter.NEWSLETTER_COMPLETED
                    newsletter.save()

            newsletters = Newsletter.objects.filter(start_time__lte=current_datetime).filter(
                end_time__gte=current_datetime).filter(
                status__in=[Newsletter.NEWSLETTER_CREATED])  # создание объекта с применением фильтра

            for newsletter in newsletters:
                newsletter.status = Newsletter.NEWSLETTER_STARTED
                try:
                    send_mail(
                        subject=Message.objects.get(pk=newsletter.id).message_title,
                        message=Message.objects.get(pk=newsletter.id).message_body,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[client.email for client in newsletter.clients.all()],
                        fail_silently=False,
                    )
                    server_response = 'ok'
                    status = 'Выполнена рассылка'
                except smtplib.SMTPException as e:
                    server_response = str(e)
                    status = 'НЕ выполнена рассылка'
                finally:
                    for client in newsletter.clients.all():
                        log = Log.objects.create(
                            time=timezone.localtime(timezone.now()),
                            status=status,
                            server_response=server_response,
                            newsletter=newsletter,
                            client=client,
                        )
                        log.save()
                if newsletter.periodicity == Newsletter.DAY_PERIODICITY:
                    newsletter.start_time += timedelta(days=1)
                elif newsletter.periodicity == Newsletter.MONTH_PERIODICITY:
                    newsletter.start_time += timedelta(days=7)
                elif newsletter.periodicity == Newsletter.WEEK_PERIODICITY:
                    newsletter.start_time += timedelta(weeks=1)
                newsletter.status = Newsletter.NEWSLETTER_CREATED
                newsletter.save()
        except Exception:
            pass
