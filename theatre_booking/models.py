import uuid
from django.db import models
import uuid
from django.db.models.base import Model
from django.db.models.fields import BooleanField, CharField, DateTimeField, SlugField, UUIDField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from theatre_booking.Languages import LANGUAGES

from django.db.models.deletion import DO_NOTHING
from users.models import CustomUser
from django.db.models.fields import UUIDField
# Create your models here.

class Region(models.Model):
    id = UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    city_name = SlugField(max_length=255, unique=True)
    state_name = CharField(max_length=255,)
    country_name = CharField(max_length=255,)
    date_created = DateTimeField(auto_now_add=True,)

    def __str__(self):
        return ('{}, {}, {}'.format(self.city_name, self.state_name, self.country_name))


class Genre(models.Model):
    id = UUIDField(default=uuid.uuid4, primary_key=True, editable=False,)
    name = CharField(max_length=20,)

    def __str__(self):
        return self.name


class Movie(models.Model):
    CERTIFICATION = (
        ('U', 'U'),
        ('UA', 'UA'),
        ('A', 'A'),
        ('S', 'S')
    )
    FORMAT = (
        ('2D', '2D'),
        ('3D', '3D'),
        ('I2D', 'IMAX 2D'),
        ('I3D', 'IMAX 3D'),
        ('4D', '4D'),
        ('4DX', '4DX'),
        ('insignia', 'Insignia')
    )

    id = UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = SlugField(max_length=255)
    format = CharField(max_length=10, choices=FORMAT)
    language = CharField(max_length=100, choices=LANGUAGES)
    certification = CharField(max_length=20, choices=CERTIFICATION)
    genre_id = ManyToManyField(Genre, null=True)
    in_theatres = BooleanField(default=True)
    date_created = DateTimeField(auto_now_add=True,)

    def __str__(self):
        return ('{} {} {}'.format(self.name, self.format, self.language))


class Theatre(models.Model):
    id = UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = CharField(max_length=255,)
    region_id = ForeignKey(Region, on_delete=models.PROTECT)
    date_created = DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.name

class Screen(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=10)
    theatre_id = models.ForeignKey(Theatre, on_delete=models.CASCADE)

class Showtime(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_time = models.DateTimeField(auto_now_add=False, auto_now=False)
    end_time = models.DateTimeField(auto_now_add=False, auto_now=False)
    theatre_id = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    screen_id = models.ForeignKey(Screen, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)



class Seat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seat_row = models.CharField(max_length=5)
    seat_column = models.PositiveIntegerField()
    is_booked = models.BooleanField(default=False, null=False)
    Ticket_id = models.ForeignKey(Ticket, on_delete=models.SET_NULL)
    price = models.FloatField()
    checkout_id = models.CharField()

    def save(self, *args, **kwargs):
        if self.checkout_id is not None:
            self.is_booked = True


class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_created=True)
    


