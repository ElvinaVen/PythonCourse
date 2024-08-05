import smtplib
from datetime import datetime, timedelta

import pytz
from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail

from main.models import Newsletter, Message, Log
from apscheduler.schedulers.background import BackgroundScheduler

from config.settings import CACHE_ENABLED


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
        log = Log.objects.create(newsletter=objects, server_response=e)
        log.save()


def send_newsletter_periodic_email():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    print(f'Текущее время - {current_datetime}')

    for obj in Newsletter.objects.filter(status__in=('создана', 'запущена')):
        if obj.start_time < current_datetime < obj.end_time:

            log = Log.objects.filter(newsletter=obj)
            if log.exists():
                last_log = log.order_by('time').last()
                current_timedelta = current_datetime - last_log.time

                if obj.periodicity == 'day' and current_timedelta >= timedelta(days=1):
                    send_newsletter_email(obj)
                    print(f'Выполнена рассылка раз в день')
                elif obj.periodicity == 'week' and current_timedelta >= timedelta(weeks=1):
                    send_newsletter_email(obj)
                    print(f'Выполнена рассылка раз в неделю')
                elif obj.periodicity == 'month' and current_timedelta >= timedelta(
                        weeks=4):
                    send_newsletter_email(obj)
                    print(f'Выполнена рассылка раз в месяц')
                elif obj.periodicity == 'minute' and current_timedelta >= timedelta(minutes=1):
                    send_newsletter_email(obj)
                    print(f'Выполнена рассылка раз в минуту')
            else:
                send_newsletter_email(obj)
                print(f'иначе')
        elif current_datetime > obj.end_time:
            obj.status = 'завершена'
            obj.save()


def start_scheduler():
    scheduler = BackgroundScheduler()

    # Проверка, добавлена ли задача уже
    if not scheduler.get_jobs():
        scheduler.add_job(send_newsletter_periodic_email, 'interval', seconds=3600)

    if not scheduler.running:
        scheduler.start()


def get_newsletter_from_cache():
    """
    Получение списка рассылок из кэша. Если кэш пуст,то получение из БД.
    """
    if not CACHE_ENABLED:
        return Newsletter.objects.all()
    else:
        key = 'newsletters_list'
        newsletter = cache.get(key)
        if newsletter is not None:
            return newsletter
        else:
            newsletter = Newsletter.objects.all()
            cache.set(key, newsletter)
            return newsletter
