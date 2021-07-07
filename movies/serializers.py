from django.db.models import fields
from rest_framework import serializers

from .models import *


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('genre',)

        

class MovieSerializerResponse(serializers.ModelSerializer):
    genre_name = GenreSerializer(many=True, source='genre', read_only=True)
    

    class Meta:
        model = Movie
        fields = [
            'id', 
            'name',
            'release_date',
            'language',
            'format',
            'length',
            'certification',
            'movie_cover',
            'genre_name'
        ]