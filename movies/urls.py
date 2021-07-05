from django.urls import path

from . import views

urlpatterns =[
    path('api/movies', views.MovieListView.as_view())
]