from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


app_name = "api_moves"

router = DefaultRouter()
router.register('', views.TodosViewSetApiView)

urlpatterns = [
    path('', include(router.urls)),
    
]
