from django.conf import settings
from django.core.mail import send_mail

from order.models import Order


def send_order_email(order_item: Order):

    send_mail(
        'Заявка на покупку лодки',
        f'{order_item.name} ({order_item.email}) желает купить вашу лодку {order_item.boat.name}. Вот сообщение: {order_item.message}',
        settings.EMAIL_HOST_USER,
        [order_item.boat.owner.email],

    )