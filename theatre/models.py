import uuid
from django.core import validators
from django.db.models.expressions import F
import django.utils.timezone
from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from cities_light.models import Country, Region, City
from smart_selects.db_fields import ChainedForeignKey
from djmoney.models.fields import MoneyField
from movies.models import Movie
# Create your models here.


class Theatre(models.Model):
    """A Theatre table containing all Theatres"""
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4)
    name = models.CharField(max_length=200, null=True)
    screen_number = models.PositiveIntegerField(
        verbose_name="number of screens")
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    state_region = ChainedForeignKey(
        Region, chained_field="country",
        chained_model_field="country",
        show_all=False,
        auto_choose=True,
        sort=True,
        verbose_name="state/region",
        on_delete=models.SET_NULL,
        null=True)
    city = ChainedForeignKey(
        City, chained_field="state_region",
        chained_model_field="region",
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.SET_NULL,
        null=True)
    pincode = models.CharField(max_length=15)
    address = models.CharField(max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        lst_str = str(self.id).split('-')
        code = "".join(lst_str[:2])
        return ("{}-{}".format(self.name, code))

    class Meta:
        ordering = ['date_created']


class Screen(models.Model):

    FORMAT = (
        ('2D', '2D'),
        ('3D', '3D'),
        ('I2D', 'IMAX 2D'),
        ('I3D', 'IMAX 3D'),
        ('4D', '4D'),
        ('4DX', '4DX'),
        ('insignia', 'Insignia')
    )

    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    screen_name = models.CharField(max_length=10)
    theatre_id = models.ForeignKey(
        Theatre, to_field="id", on_delete=models.CASCADE,)
    screen_format = models.CharField(max_length=20, choices=FORMAT)
    seats = models.PositiveIntegerField(verbose_name="number of seats")
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        lst_str = str(self.id).split('-')
        code = "".join(lst_str[0])
        return ("S#{}".format(code))

    class Meta:
        ordering = ['date_created']


class Seat(models.Model):
    upercase_alpha = RegexValidator(
        r'^[A-Z]*$', 'Only Alphabetic(Uppercase/Capital) characters are allowed.')

    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, editable=False,)
    row = models.CharField(max_length=10, validators=[upercase_alpha])
    seat_number = models.PositiveIntegerField()
    cost = MoneyField(max_digits=10, decimal_places=2, default_currency='INR')
    screen_id = models.ForeignKey(Screen,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['date_created']
        unique_together = [['row', 'seat_number', 'screen_id']]


class ScreeningTime(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    theatre_id = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    screen_id = ChainedForeignKey(Screen, chained_field='theatre_id',
                                  chained_model_field='theatre_id', show_all=False, auto_choose=True, sort=True)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    scheduled_date = models.DateField(default=django.utils.timezone.now)
    start_time = models.TimeField(default=django.utils.timezone.now)
    end_time = models.TimeField(default=django.utils.timezone.now)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return ('{}, {}-{}'.format(self.scheduled_date, self.start_time, self.end_time))

    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError('Start Time should be before End Time')
        return super().clean()

    class Meta:
        unique_together = [['scheduled_date', 'screen_id', 'start_time', ]]
