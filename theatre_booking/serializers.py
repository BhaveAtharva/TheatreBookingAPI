from django.db import models
from django.db.models import fields
from rest_framework.fields import SerializerMethodField
from theatre_booking.models import Movie, Region, Showtime, Theatre
from rest_framework import serializers


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        # fields = ['id', 'city_name', 'state_name', 'country_name']
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(
        many=True, source='genre_id', read_only=True)
    regions = serializers.PrimaryKeyRelatedField(
        many=True, source='region_id', read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'name', 'release_date', 'length', 'format', 'language',
                  'certification', 'movie_cover', 'genres', 'regions', 'in_theatres', ]


class ShowtimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Showtime
        # fields = ('id', 'start_time', 'end_time', 'theatre_id',
        #           'screen_id', 'movie_id', 'date_created')
        fields = ('__all__')


class MethodField(SerializerMethodField):
    def __init__(self, method_name=None, **kwargs):
        super().__init__(method_name=method_name, **kwargs)
        self.func_kwargs = kwargs

    def to_representation(self, value):
        method = getattr(self.parent, self.method_name)
        return method(value, **self.func_kwargs)


class TheatreSerializer(serializers.ModelSerializer):
    # movie = serializers.StringRelatedField(
    #     many=True, source='movie_id', read_only=True)
    all_showtime = MethodField('get_shows')

    def get_shows(self, obj, **kwargs):
        movie_id = self.context.get('movie_id')
        queryset = Showtime.objects.filter(
            theatre_id=obj.id).filter(movie_id=movie_id)
        return ShowtimeSerializer(queryset, many=True).data

    class Meta:
        model = Theatre
        fields = ['id', 'name', 'region_id', 'all_showtime', 'date_created']


# class CustomSerializer(serializers.Se)
