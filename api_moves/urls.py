from django.urls import path
from .views import *


urlpatterns = [
    path('rrr', csv_to_db),
]
