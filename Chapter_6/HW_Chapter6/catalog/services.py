from django.conf import settings
from django.core.cache import cache

from catalog.models import Product


def get_cached_products():
    ''' Получает данные по подуктам из кеша, если кеш пуст, то получает из БД '''
    if settings.CACHE_ENABLED:
        key = f'subject_list'
        subject_list = cache.get(key)
        if subject_list is None:
            subject_list = Product.objects.all()
            cache.set(key, subject_list)
    else:
        subject_list = Product.objects.all()
    return subject_list