from django.contrib import admin

from boat.models import Boat, Owner, BoatHistory


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Boat)
class BoatAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'owner', )
    search_fields = ('owner',)
    list_filter = ('year', 'owner',)


@admin.register(BoatHistory)
class BoatHistoryAdmin(admin.ModelAdmin):
    list_display = ('boat', 'start_year', 'stop_year', 'owner', )
    search_fields = ('owner',)
    list_filter = ('boat', 'owner',)