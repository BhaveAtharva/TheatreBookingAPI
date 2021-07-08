from django.contrib import admin

# Register your models here.
from .models import Reservation, SeatReservationHistory, SeatsReserved


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'theatre_id', 'screen_id',
                    'screening_time_id', 'total_price', 'paid', 'reservation_is_active', ]


class SeatReservedAdmin(admin.ModelAdmin):
    list_display = ['seats_reserved_id', 'seat_id', 'show_time_id', 'reservation_id', 'is_reserved']


class SeatReservationHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'seat_id',
                    'seat_id', 'screen_id', 'screening_time_id', ]


admin.site.register(Reservation, ReservationAdmin)
admin.site.register(SeatsReserved, SeatReservedAdmin)
admin.site.register(SeatReservationHistory, SeatReservationHistoryAdmin)
