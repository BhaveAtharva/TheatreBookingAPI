from theatre.models import Theatre
from django.db.models import fields
from rest_framework import serializers

from .models import SeatsReserved, Reservation

from theatre.serializers import SeatSerializer, TheatreSerializer, ScreeningTimeSerializer

class SeatsReservedSerializer(serializers.ModelSerializer):
    
    seat = SeatSerializer(source='seat_id')
    
    # theatre = TheatreSerializer(source='theatre_id', read_only=True)
    
    # show_time = ScreeningTimeSerializer(source='show_time_id', read_only =True)

    class Meta:
        model = SeatsReserved
        fields = [
            'seats_reserved_id',
            'is_reserved',
            'payment_processing',
            'seat'
        ]

# class SeatsBookedSerializer(serializers.ModelSerializer):
#     seat = SeatSerializer(source='seat_id', many=True)

#     class Meta:
#         model = 

class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = [
            'user_id',
            'movie_id',
            'theatre_id',
            'screen_id',
            'screening_time_id',
            'total_price',
            'paid',
            'reservation_is_active',
            'date_created',
        ]

class ResrvationDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = [

        ]