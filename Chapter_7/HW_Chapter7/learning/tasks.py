from celery import shared_task
from django.core.mail import send_mail
from config import settings

from django.utils import timezone
from datetime import timedelta
from learning.models import Subscription, Course

from users.models import User


@shared_task
def send_email(course_id):
    try:
        course = Course.objects.get(pk=course_id)
        subscribers = Subscription.objects.get(course=course_id)

        print("Отправка работает")

        send_mail(
            subject=f'Курс {course} обновлен',
            message=f'Курс {course}, на который вы подписаны, обновлен',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[subscribers.user.email]
        )
    except Course.DoesNotExist:
        print(f"Курс с id={course_id} не найден.")
    except Subscription.DoesNotExist:
        print(f"Подписчики на курс с id={course_id} не найдены.")


@shared_task
def deactivate_user():
    """
    Проверка пользователей по дате последнего входа и, если пользователь не заходил более месяца, блокировка его.
    """
    users = User.objects.filter(is_active=True, is_superuser=False, last_login__isnull=False)
    print(users)
    if users.exists():
        for user in users:
            print(user.last_login)
            if user.last_login < (timezone.now() - timedelta(days=30)):
                user.is_active = False
                print(f'{user} отключен')
                user.save()
