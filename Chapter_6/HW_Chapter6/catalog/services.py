from django.conf import settings
from django.core.cache import cache

from catalog.models import Product


def get_cached_products():
    if settings.CACHE_ENABLED:
        key = f'subject_list_{student_pk}'
        subject_list = cache.get(key)
        if subject_list is None:
            subject_list = Product.objects.filter(student__pk=student_pk)
            cache.set(key, subject_list)
    else:
        subject_list = Product.objects.filter(student__pk=student_pk)
    return subject_list