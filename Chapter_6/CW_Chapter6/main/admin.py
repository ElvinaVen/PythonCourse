from django.contrib import admin

from main.models import Client, Message, Newsletter, Log


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'comment',)
    list_filter = ('first_name',)
    search_fields = ('first_name', 'email',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_title', 'message_body',)
    list_filter = ('message_title',)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('newsletter_name', 'periodicity', 'status', 'message',)
    list_filter = ('newsletter_name', 'status',)


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('time', 'server_response', 'status', 'newsletter',)
    list_filter = ('status', 'newsletter',)
