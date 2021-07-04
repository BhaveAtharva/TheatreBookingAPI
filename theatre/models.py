import uuid
from django.db import models
from cities_light.models import Country, Region, City
from smart_selects.db_fields import ChainedForeignKey
# Create your models here.


class Theatre(models.Model):
    """A Theatre table containing all Theatres"""
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4)
    name = models.CharField(max_length=200, null=True)
    screen_number = models.IntegerField(verbose_name="number of screens")
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
        return str(self.name)


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
    theatre_id = models.ForeignKey(
        Theatre, to_field="id", on_delete=models.SET_NULL, null=True)
    screen_format = models.CharField(max_length=20, choices=FORMAT)
    seats = models.IntegerField(verbose_name="number of seats")
