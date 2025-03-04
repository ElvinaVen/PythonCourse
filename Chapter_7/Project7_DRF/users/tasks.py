import datetime
from celery import shared_task
from users.models import User


@shared_task
def my_task():
    """
    �������� ������������� �� ���� ���������� ����� �, ���� ������������ �� ������� ����� ������, ���������� ���.
    """
    users = User.objects.all()
    today = datetime.date.today()
    deactivate_time = datetime.timedelta(days=30)
    for user in users:
        if today - user.last_login > deactivate_time:
            user.is_active = False
            print(f'{user} ��������')
            user.save()


# def my_task():
#     today = datetime.date.today()
#     print(today)

#celery -A config beat -l info -S django