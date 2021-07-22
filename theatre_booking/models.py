import uuid
from django.db import models
import uuid
import django.utils.timezone
from django.db.models.base import Model
from django.db.models.fields import BooleanField, CharField, DateTimeField, SlugField, UUIDField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.core.validators import RegexValidator
from rest_framework.fields import DurationField
from theatre_booking.Languages import LANGUAGES
from mptt.models import MPTTModel, TreeForeignKey
from django.db.models.deletion import DO_NOTHING
from users.models import CustomUser
from django.db.models.fields import UUIDField
from django.core.exceptions import ValidationError
# Create your models here.


class Region(models.Model):
    id = UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    city_name = SlugField(max_length=255, unique=True)
    state_name = CharField(max_length=255,)
    country_name = CharField(max_length=255,)
    date_created = DateTimeField(auto_now_add=True, null=True)

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
    release_date = models.DateTimeField(default=django.utils.timezone.now)
    length = models.DurationField(default='00:00:00')
    format = CharField(max_length=10, choices=FORMAT)
    language = CharField(max_length=100, default='en', choices=LANGUAGES)
    certification = CharField(max_length=20, choices=CERTIFICATION)
    movie_cover = ImageField(upload_to='movie_covers/', null=True)
    genre_id = ManyToManyField(Genre, null=True)
    region_id = ManyToManyField(Region, null=True, blank=True)
    in_theatres = BooleanField(default=True)
    date_created = DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return ('{} {} {}'.format(self.name, self.format, self.language))


class Theatre(models.Model):
    id = UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = CharField(max_length=255,)
    region_id = ForeignKey(Region, on_delete=models.PROTECT)
    movie_id = ManyToManyField(Movie, null=True, blank=True)
    date_created = DateTimeField(auto_now_add=True, null=True)

    # def __str__(self):
    #     return self.name

    def __str__(self):
        lst_str = str(self.id).split('-')
        code = "".join(lst_str[:2])
        return ("{}-{}".format(self.name, code))


class Screen(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=10)
    theatre_id = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return ("{}-{}".format(self.name, self.theatre_id))


class Showtime(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_time = models.DateTimeField(auto_now_add=False, auto_now=False)
    end_time = models.DateTimeField(auto_now_add=False, auto_now=False)
    theatre_id = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    screen_id = models.ForeignKey(Screen, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    # def __str__(self):
    #     return str(self.start_time)

    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError('Start Time should be before End Time')
        return super().clean()

    class Meta:
        unique_together = [['start_time', 'screen_id']]


class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT, null=True)
    created = models.DateTimeField(auto_created=True)


class Seat(models.Model):
    upercase_alpha = RegexValidator(
        r'^[A-Z]*$', 'Only Alphabetic(Uppercase/Capital) characters are allowed.')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seat_row = models.CharField(max_length=5, validators=[upercase_alpha])
    seat_column = models.PositiveIntegerField()
    is_booked = models.BooleanField(default=False,)
    ticket_id = models.ForeignKey(
        Ticket, blank=True, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    checkout_id = models.CharField(max_length=255, blank=True, null=True)
    showtime_id = models.ForeignKey(
        Showtime, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        if self.checkout_id is not None:
            self.is_booked = True
        return super(Seat, self).save(*args, **kwargs)

    def __str__(self):
        return '{} {}'.format(self.seat_row, self.seat_column)

    class Meta:
        unique_together = [['showtime_id', 'seat_row', 'seat_column']]


class UserReview(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4)
    review = models.TextField()
    rating = models.FloatField()
    review_date = models.DateTimeField(auto_now_add=True)
    movie_id = models.ForeignKey(
        Movie, on_delete=models.CASCADE, verbose_name='Movie')
    user_id = models.ForeignKey(
        CustomUser, null=True, on_delete=models.SET_NULL, verbose_name='user')

    def __str__(self):
        return str(self.user_id)


class Comments(MPTTModel):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4)
    user_review = models.ForeignKey(
        UserReview, null=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey(
        CustomUser, null=True, on_delete=models.SET_NULL)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str('comment by '+str(self.user_id))
