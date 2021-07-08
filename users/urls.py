from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'users', views.CustomUserViewset)
# router.register(r'customuser', views.CustomUserRegisterViewSet)
# router.register(r'movies/staff', views.MovieStaffViewSet)

urlpatterns =[
    path('', include(router.urls))
]