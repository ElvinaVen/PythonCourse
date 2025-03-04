from django.contrib import admin
from users.models import User


# Register your models here.
admin.site.register(User)



class Admin(admin.ModelAdmin):
    list_display = (
        "user",
        "email",

    )
