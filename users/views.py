from django.shortcuts import render

# Create your views here.
# from .serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework import permissions

from .models import CustomUser

# class CustomUserViewset(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer