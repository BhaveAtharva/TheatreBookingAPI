from django.contrib import admin

# Register your models here.
from .models import Screening, Seat, Theatre, Screen


class TheatreAdmin(admin.ModelAdmin):
    list_display = ['name', '__str__', 'screen_number',
                    'date_created', 'city', 'state_region', 'country', 'pincode', 'address']


class ScreenAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'screen_name',
                    'theatre_id', 'screen_format', 'seats', 'date_created', ]
    radio_fields = {'screen_format': admin.HORIZONTAL}


class SeatAdmin(admin.ModelAdmin):
    list_display = ['id', 'row',
                    'seat_number', 'screen_id', 'theatre_id', 'cost', 'reservation_id', 'is_reserved']


class ScreeningAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__', 'scheduled_date', 'start_time', 'end_time', 'theatre_id',
                    'screen_id', 'movie_id', 'date_created', ]


admin.site.register(Theatre, TheatreAdmin)
admin.site.register(Screen, ScreenAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Screening, ScreeningAdmin)
