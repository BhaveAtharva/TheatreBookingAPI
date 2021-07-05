from django.shortcuts import render
from .serializers import *
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from .models import *

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serialized = MovieSerializerResponse(queryset, many=True)

        return Response(data=serialized.data, status=status.HTTP_200_OK)

# class MovieView(APIView):

#     def get()
