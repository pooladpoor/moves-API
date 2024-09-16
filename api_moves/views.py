from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer


class TodosViewSetApiView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

