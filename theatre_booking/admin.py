from django.contrib import admin
from .models import Genre, Movie, Region, Screen, Seat, Showtime, Theatre, Ticket, UserReview, Comments  
# Register your models here.
class RegionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'city_name',
        'state_name',
        'country_name',
        'date_created',
    ]

class GenreAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]

class MovieAdmin(admin.ModelAdmin):
        
    list_display = [
        'id',
        'name',
        'format',
        'language',
        'certification',
        'genres',
        'in_theatres',
        'date_created',
    ]
    def genres(self, obj):
        genres = obj.genre_id.all()
        genres = ', '.join([str(i) for i in genres])
        return genres

class TheatreAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'region_id',
        'date_created',
    ]

class ScreenAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'theatre_id',
    ]

class ShowtimeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'start_time',
        'end_time',
        'theatre_id',
        'screen_id',
        'movie_id',
    ]

class TicketAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user_id',
        'created',
    ]

class SeatAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'seat_row',
        'seat_column',
        'is_booked',
        'ticket_id',
        'price',
        'checkout_id',
    ]

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
