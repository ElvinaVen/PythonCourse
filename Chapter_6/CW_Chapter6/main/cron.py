import smtplib
from datetime import datetime, timedelta

import pytz
from django.conf import settings
from django.core.mail import send_mail

from main.models import Newsletter, Message, Log


def send_newsletter_email(objects):
    try:
        message_instance = Message.objects.first()  # Замени на подходящий запрос
        server_response = send_mail(
            subject=message_instance.message_title,
            message=message_instance.message_body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[client.email for client in objects.client.all()],
            fail_silently=False,
        )
        log = Log.objects.create(newsletter=objects, server_response=server_response)
        if server_response:
            log.status = 'Успешно'
            log.save()
        if objects.status == 'создана':
            objects.status = 'запущена'
            objects.save()
    except smtplib.SMTPException as e:
        log=Log.objects.create(newsletter=objects, server_response=e)
        log.save()


def send_newsletter_periodic_email():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    print(f'дата - {current_datetime}')

    for obj in Newsletter.objects.filter(status__in=('создана', 'запущена')):
        if obj.start_time < current_datetime < obj.end_time:

            log = Log.objects.filter(newsletter=obj)
            print(f'первый - {log}')
            if log.exists():
                last_log = log.order_by('time').last()
                current_timedelta = current_datetime - last_log.time
                print(current_timedelta)

                if obj.periodicity == 'day' and current_timedelta <= timedelta(days=1):
                    send_newsletter_email(obj)
                    print(f'раз в день')
                elif obj.periodicity == 'week' and current_timedelta >= timedelta(weeks=1):
                    send_newsletter_email(obj)
                    print(f'раз в неделю')
                elif obj.periodicity == 'month' and current_timedelta >= timedelta(
                        weeks=4):
                    send_newsletter_email(obj)
                    print(f'раз в месяц')
                elif obj.periodicity == 'minute' and current_timedelta >= timedelta(minutes=1):
                    send_newsletter_email(obj)
                    print(f'раз в minute')
            else:
                send_newsletter_email(obj)
                print(f'иначе')
        elif current_datetime > obj.end_time:
            obj.status = 'завершена'
            obj.save()
