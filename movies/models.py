from django.db import models
import uuid
from .Languages import LANGUAGES
from .Genres import GENRES
# Create your models here.


class Genre(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    genre = models.CharField(max_length=20)

    def __str__(self):
        return self.genre


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

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    release_date = models.DateTimeField()
    language = models.CharField(max_length=20, default='en', choices=LANGUAGES)
    format = models.CharField(max_length=20, choices=FORMAT)
    length = models.DurationField()
    certification = models.CharField(max_length=20, choices=CERTIFICATION)
    movie_cover = models.ImageField(upload_to='movie_covers/', null=True)
    genre = models.ManyToManyField(Genre, null=True)

    def __str__(self):
        return str(self.name+' '+self.format+' '+self.language)
