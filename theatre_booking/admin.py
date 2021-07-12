from django.db import models
from django.forms import CheckboxSelectMultiple
from theatre_booking.models import Genre, Movie, Region, Screen, Seat, Showtime, Theatre, Ticket
from django.contrib import admin

# Register your models here.


class RegionAdmin(admin.ModelAdmin):
    model = Region
    list_display = ['id', 'city_name', 'state_name',
                    'country_name', 'date_created']


class MovieAdmin(admin.ModelAdmin):
    model = Movie
    list_display = ['id', 'name', 'format', 'language',
                    'certification', 'genres', 'in_theatres', 'date_created']

    def genres(self, obj):
        genres = obj.genre.all()
        genres = ', '.join([str(i) for i in genres])
        return genres

    formfield_overrides = {
        models.ManyToManyField: {
            'widget': CheckboxSelectMultiple
        }
    }
    radio_fields = {'format': admin.HORIZONTAL}


class MovieInline(admin.TabularInline):
    model = Movie.genre_id.through


class GenreAdmin(admin.ModelAdmin):
    model = Genre
    inlines = [
        MovieInline
    ]


class TheatreAdmin(admin.ModelAdmin):
    model = Theatre
    list_display = ['id', 'name', 'region_id', 'date_created']


class ScreenAdmin(admin.ModelAdmin):
    model = Screen
    list_display = ['id', 'name', 'theatre_id', 'date_created']


class ShowTimeAdmin(admin.ModelAdmin):
    model = Showtime
    list_display = ['id', 'start_time', 'end_time',
                    'theatre_id', 'screen_id', 'movie_id', 'date_created']


class SeatAdmin(admin.ModelAdmin):
    model = Screen
    list_display = ['id', 'seat_row', 'seat_column',
                    'is_booked', 'ticket_id', 'price', 'checkout_id']


class TicketAdmin(admin.ModelAdmin):
    model = Screen
    list_display = ['id', 'user_id', 'created', ]


admin.site.register(Region, RegionAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)
admin.site.register(Theatre, TheatreAdmin)
admin.site.register(Screen, ScreenAdmin)
admin.site.register(Showtime, ShowTimeAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Ticket, TicketAdmin)
