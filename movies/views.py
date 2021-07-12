# from django.shortcuts import render
# from django.views.generic.base import View
# from .serializers import MovieSerializerResponse
# # Create your views here.
# from rest_framework.response import Response
# from rest_framework import viewsets, mixins
# from rest_framework import permissions

# from .models import Movie


# class MovieViewSet(viewsets.ModelViewSet):
    
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializerResponse

#     def get_permissions(self):
#         if self.action in ('create', 'update', 'partial_update', 'destroy'):
#             self.permission_classes = [permissions.IsAdminUser,]
#         elif self.action in ('list', 'retrieve'):
#             self.permission_classes = [permissions.IsAuthenticated,]
#         return super().get_permissions()


