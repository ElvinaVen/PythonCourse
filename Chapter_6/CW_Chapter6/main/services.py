from datetime import timezone
from smtplib import SMTPException

from django.conf import settings
from django.core.mail import send_mail

from main.models import Newsletter


def send_mailing():
    '''Главная функция по отправке рассылки'''
    current_time = timezone.localtime(timezone.now())
    newsletter_list = Newsletter.objects.all()

    for newsletter in newsletter_list:
        if newsletter.date_end < current_time:
            newsletter.status = Newsletter.DONE
            continue
        if newsletter.time_start <= current_time < newsletter.date_end:
            newsletter.status = Newsletter.STARTED
            newsletter.save()
            # for client in newsletter.client.all():
            #     try:
            #         send_mail(
            #             subject=newsletter.message.message_title,
            #             message=newsletter.message.message_body,
            #             from_email=settings.EMAIL_HOST_USER,
            #             recipient_list=[client.email],
            #             fail_silently=False
            #         )

                    # log = Logs.objects.create(
                    #     date=newsletter.time_start,
                    #     status=Logs.SENT,
                    #     mailing=newsletter,
                    #     client=client
                    # )
                    # log.save()
                    # return log

                # except SMTPException as error:
                #     log = Logs.objects.create(
                #         date=newsletter.time_start,
                #         status=Logs.FAILED,
                #         mailling=newsletter,
                #         client=client,
                #         response=error
                #     )
                #     log.save()
                #
                #     return log

        else:
            newsletter.status = Newsletter.DONE
            newsletter.save()
