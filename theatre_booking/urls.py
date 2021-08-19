from django.conf.urls import url
from django.urls import path, include

from . import views
urlpatterns = [
    path('home/', views.HomeViewsets.as_view({'get': 'home_region'})),
    path('home/<slug:region>/movies/',
         views.HomeViewsets.as_view({'get': 'home_movies'})),
    path('home/<slug:region>/movies/<str:id>/showtime/',
         views.ShowtimeViewsets.as_view({'get': 'choose_theatre_showtime'})),
    # path('movies/', views.MovieViewsets.as_view({'get': 'get_movies'})),
]
