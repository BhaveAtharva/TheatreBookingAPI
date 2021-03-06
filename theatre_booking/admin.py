from django.db import models
from django.forms import CheckboxSelectMultiple
# from theatre_booking.models import Genre, Movie, Region, Screen, Seat, Showtime, Theatre, Ticket
from django.contrib import admin
from .models import Genre, Movie, Region, Screen, Seat, Showtime, Theatre, Ticket, UserReview, Comments
# Register your models here.


class RegionAdmin(admin.ModelAdmin):
    model = Region
    list_display = ['id', 'city_name', 'state_name',
                    'country_name', 'date_created']


class MovieAdmin(admin.ModelAdmin):
    model = Movie
    list_display = ['id', 'name', 'release_date', 'length', 'format', 'language',
                    'certification', 'movie_cover', 'genres', 'regions', 'in_theatres', ]

    def genres(self, obj):
        genres = obj.genre_id.all()
        genres = ', '.join([str(i) for i in genres])
        return genres

    def regions(self, obj):
        regions = obj.region_id.all()
        return (', '.join([str(i) for i in regions]))

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
    list_display = ['id', 'name', 'region_id', 'movies', 'date_created']

    def movies(self, obj):
        movies = obj.movie_id.all()
        return (', '.join([str(i) for i in movies]))

    formfield_overrides = {
        models.ManyToManyField: {
            'widget': CheckboxSelectMultiple
        }
    }


class ScreenAdmin(admin.ModelAdmin):
    model = Screen
    list_display = ['id', 'name', 'theatre_id', 'date_created']


class ShowtimeAdmin(admin.ModelAdmin):
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


class UserReviewAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'review',
        'rating',
        'review_date',
        'movie_id',
        'user_id',
    ]


class CommentsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user_review',
        'user_id',
        'parent',
        'comment',
        'comment_date',
    ]


admin.site.register(Region, RegionAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Theatre, TheatreAdmin)
admin.site.register(Screen, ScreenAdmin)
admin.site.register(Showtime, ShowtimeAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(UserReview, UserReviewAdmin)
admin.site.register(Comments, CommentsAdmin)
