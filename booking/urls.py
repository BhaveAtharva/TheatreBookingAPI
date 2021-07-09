from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter


urlpatterns =[
    path('reservedseats/<str:show_id>/', views.SeatReservedViewset.as_view({'get': 'get_seats_reserved'})),
    path('reservedseats/', views.SeatReservedViewset.as_view({'patch': 'patch_seats_reserved'})),
    path('reservation/', views.ReservationViewSet.as_view({'post': 'post_reservation'}))
]