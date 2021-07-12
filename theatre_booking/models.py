from django.db import models
import uuid

from django.db.models.deletion import DO_NOTHING
from users.models import CustomUser
from django.db.models.fields import UUIDField
# Create your models here.

class Showtime(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_time = models.DateTimeField(auto_now_add=False, auto_now=False)
    end_time = models.DateTimeField(auto_now_add=False, auto_now=False)
    theatre_id = models.ForeignKey(Theare, on_delete=models.CASCADE)
    screen_id = models.ForeignKey(Screen, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)

class Screen(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=10)
    theatre_id = models.ForeignKey(Theatre, on_delete=models.CASCADE)

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
    

