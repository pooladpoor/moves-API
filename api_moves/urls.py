from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


app_name = "api_moves"


urlpatterns = [
    path('', views.MoviesListApiView.as_view()),
    path('/<int:movie_id>', views.MoviesDetailApiView.as_view()),
]
