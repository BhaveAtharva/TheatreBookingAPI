import uuid
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import BooleanField, CharField, DateTimeField, SlugField, UUIDField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from theatre_booking.Languages import LANGUAGES

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
    genre_id = ManyToManyField(Genre)
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
