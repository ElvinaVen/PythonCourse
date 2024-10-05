from celery import shared_task

from config import settings
import pytz
from datetime import datetime, timedelta

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task()
def telegram_notification():
    print('таска')
    zone = pytz.timezone(settings.TIME_ZONE)  # получить текущую временную зону, указанную в настройках приложения
    current_time = datetime.now(zone)  # Здесь создаётся переменная current_time, которая содержит текущее время с
    # учётом указанной временной зоны
    print(current_time)
    current_time_less = current_time - timedelta(minutes=5)  # В этой строке вычисляется время, которое было 5 минут
    # назад, и сохраняется в переменной current_time_less. Это нужно, чтобы получить привычки, которые должны быть
    # выполнены в последние 5 минут
    habits = Habit.objects.filter(time__lte=current_time.time(), time__gte=current_time_less.time())
    for habit in habits:
        user_tg = habit.user.tg_chat_id
        message = f"я буду {habit.action} в {habit.time} в {habit.place}"
        send_telegram_message(user_tg, message)  # вызов функции отправки сообщения
