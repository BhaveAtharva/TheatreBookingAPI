from django.contrib import admin

# Register your models here.
from .models import Reservation, SeatReservationHistory


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'theatre_id', 'screen_id',
                    'screening_id', 'total_price', 'paid', 'active_reservation', ]


class SeatReservationHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'seat_id',
                    'seat_id', 'screen_id', 'screening_id', ]


admin.site.register(Reservation, ReservationAdmin)
admin.site.register(SeatReservationHistory, SeatReservationHistoryAdmin)
