from django.contrib import admin
from users.models import User, Payment


# Register your models here.
admin.site.register(User)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "payment_date",
        "paid_course",
        "paid_lesson",
        "payment_amount",
        "payment_type",
    )
