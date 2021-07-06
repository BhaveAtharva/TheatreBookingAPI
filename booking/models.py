from django.db.models.fields import DateField, DateTimeField
from movies.models import Movie
import uuid
# from django.contrib.auth.models import User
from django.db import models
from theatre.models import Screen, Screening, Seat, Theatre
from smart_selects.db_fields import ChainedForeignKey
from users.models import CustomUser
from djmoney.models.fields import MoneyField
# Create your models here.


class Reservation(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, editable=False,)
    user_id = models.ForeignKey(
        CustomUser, null=True, on_delete=models.SET_NULL, verbose_name='user')
    movie_id = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)
    theatre_id = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    screen_id = ChainedForeignKey(Screen, chained_field='theatre_id', chained_model_field='theatre_id',
                                  show_all=False, auto_choose=True, sort=True, on_delete=models.CASCADE)
    screening_id = models.ForeignKey(
        Screening, on_delete=models.SET_NULL, null=True)

    total_price = MoneyField(null=True,
                             max_digits=10, decimal_places=2, default_currency='INR')
    paid = models.BooleanField(default=False)
    active_reservation = models.BooleanField(default=True)
    date_created = DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.id)


class SeatReservationHistory(models.Model):
    id = models.AutoField(primary_key=True, editable=False,)
    seat_id = models.ForeignKey(Seat, on_delete=models.SET_NULL, null=True)
    reservation_id = models.ForeignKey(
        Reservation, on_delete=models.CASCADE, null=True)
    screen_id = models.ForeignKey(Screen, on_delete=models.SET_NULL, null=True)
    screening_id = ChainedForeignKey(Screening, chained_field='screen_id',
                                     chained_model_field='screen_id', on_delete=models.SET_NULL, null=True)
    date_created = DateTimeField(auto_now_add=True, null=True)
