from theatre_booking import serializers
from theatre_booking.models import Movie, Region, Showtime, Theatre
from theatre_booking.serializers import MovieSerializer, RegionSerializer, ShowtimeSerializer, TheatreSerializer
from django.shortcuts import render
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action, permission_classes

# Create your views here.
from rest_framework import viewsets, permissions, status


#
class HomeViewsets(viewsets.ViewSet):

    # @permission_classes = ([permissions.IsAuthenticated])
    def home_region(self, request):
        queryset = Region.objects.all()
        serializer = RegionSerializer(queryset, many=True)
        return Response(serializer.data)

    def home_movies(self, request, **kwargs):
        try:
            region = Region.objects.get(
                city_name=kwargs['region'].capitalize())
            queryset = Movie.objects.filter(
                region_id=region.id, in_theatres=True).order_by('-release_date')
            serializer = MovieSerializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response({'Message': 'City not found'}, status=status.HTTP_404_NOT_FOUND)


class ShowtimeViewsets(viewsets.ViewSet):
    # serializer_class= TheatreSerializer

    def get_theatre(self, request, **kwargs):
        print(kwargs['id'], kwargs['region'])
        region = Region.objects.get(city_name=kwargs['region'].capitalize())
        queryset = Theatre.objects.filter(region_id=region)
        context = {'movie_id': kwargs['id']}
        serilizer = TheatreSerializer(queryset, context=context, many=True)
        return Response(serilizer.data)
