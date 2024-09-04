from django.core.mail import send_mail
from vehicle.models import Moto, Car
from celery import shared_task


@shared_task
def check_milage(pk, model):
    if model == "Car":
        instance = Car.objects.filter(pk=pk).first()
    else:
        instance = Moto.objects.filter(pk=pk).first()

    if instance:
        prev_milage = -1
        for m in instance.milage.all():
            if prev_milage == -1:
                prev_milage = m.milage

            else:
                if prev_milage < m.milage:
                    print("неверный пробег")
                    break


@shared_task
def check_filter():
    print("Отчет по фильтру1")
    filter_title = {"title": "lada"}

    if Car.objects.filter(**filter_title).exists():
        print("Отчет по фильтру2")
        # send_mail(
        #     subject="Отчет по фильтру",
        #     message="У нас есть машины по вашему фильтру",
        #     from_email="admin@admin.com",
        #     recipient_list=[user.email],
        #
        # )


