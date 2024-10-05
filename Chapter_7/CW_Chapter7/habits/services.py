
import requests
from config.settings import TELEGRAM_TOKEN, TELEGRAM_URL


def send_telegram_message(chat_id, message):
    print('отправка')
    params = {
        'text': message,
        'chat_id': chat_id
        }

    url = f'{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage'
    response = requests.get(url, params=params, timeout=10)
    if not response.ok:
        raise RuntimeError("Failed to sent telegram message")

