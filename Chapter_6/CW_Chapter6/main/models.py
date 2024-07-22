from django.db import models
from django.utils import timezone

NULLABLE = {"null": True, "blank": True}


class Client(models.Model):
    """Модель для хранения информации о клиенте
    Клиенты — это те, кто получает рассылки, а пользователи — те, кто создает эти рассылки."""

    first_name = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия', **NULLABLE)
    email = models.EmailField(max_length=100, verbose_name='email', unique=True)
    comment = models.TextField(verbose_name="комментарий", **NULLABLE)

    # owner

    def __str__(self):
        return f"Клиент - {self.first_name} {self.last_name} - {self.email}"

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"


class Message(models.Model):
    """Модель для хранения информации о сообщении для рассылки"""

    message_title = models.CharField(max_length=100, verbose_name='тема письма')
    message_body = models.TextField(verbose_name='тело письма')

    # owner

    def __str__(self):
        return f"Сообщение с темой {self.message_title}"

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"


class Newsletter(models.Model):
    """Модель для хранения информации о рассылке(настройки)"""

    NEWSLETTER_STARTED = 'запущена'
    NEWSLETTER_COMPLETED = 'завершена'
    NEWSLETTER_CREATED = 'создана'

    STATUS_CHOICES = [
        (NEWSLETTER_STARTED, 'запущена'),
        (NEWSLETTER_CREATED, 'создана'),
        (NEWSLETTER_COMPLETED, 'завершена'),
    ]

    MONTH_PERIODICITY = 'month'
    DAY_PERIODICITY = 'day'
    WEEK_PERIODICITY = 'week'

    PERIODICITY_CHOICES = [
        (MONTH_PERIODICITY, 'раз в месяц'),
        (DAY_PERIODICITY, 'раз в день'),
        (WEEK_PERIODICITY, 'раз в неделю'),
    ]

    newsletter_name = models.CharField(max_length=150, verbose_name="Название рассылки")
    created_at = models.DateTimeField(verbose_name="дата и время первой отправки рассылки", **NULLABLE, default=(timezone.now() + timezone.timedelta(days=1)),)
    periodicity = models.CharField(max_length=100, verbose_name='периодичность', choices=PERIODICITY_CHOICES,
                                   default=MONTH_PERIODICITY)
    status = models.CharField(max_length=100, verbose_name='статус рассылки',
                              default=NEWSLETTER_CREATED, choices=STATUS_CHOICES)

    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение для клиентов', **NULLABLE)
    client = models.ManyToManyField(Client, verbose_name='Имена клиентов')

    # owner

    def __str__(self):
        return f"Рассылка: '{self.newsletter_name}'"

    class Meta:
        verbose_name = "рассылка"
        verbose_name_plural = "рассылки"


class Log(models.Model):
    """Модель для хранения информации о попытках рассылок (логах)"""

    LOG_SUCCESS = 'Успешно'
    LOG_FAIL = 'Неуспешно'

    STATUS_VARIANTS = [
        (LOG_SUCCESS, 'Успешно'),
        (LOG_FAIL, 'Неуспешно'),
    ]

    time = models.DateTimeField(
        verbose_name="Дата и время попытки отправки")
    status = models.CharField(max_length=50, verbose_name='Cтатус рассылки', choices=STATUS_VARIANTS)
    server_response = models.CharField(
        max_length=150, verbose_name="Ответ сервера почтового сервиса", **NULLABLE
    )
    newsletter = models.ForeignKey(Newsletter, verbose_name='рассылка для логов', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return (f"Рассылка {self.newsletter} от {self.time} со статусом: {self.status}. Ответ сервера почтового "
                f"сервиса:{self.server_response}")

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылки"
