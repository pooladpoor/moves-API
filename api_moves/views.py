from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie
from .serializers import MovieSerializer


class MoviesListApiView(APIView):

    def get(self, request: Request):
        """
        get all movies (5 on each page) \n
        The link of the previous and next page is in JSON
        """
        movies = Movie.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 5  # تعداد آیتم هر صفحه
        paginated_queryset = paginator.paginate_queryset(movies, request)
        serializer = MovieSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    def post(self, request: Request):
        """
        add movie \n
        In the body of the request, put a json with the format of jsons received from the server
        """
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(None, status.HTTP_400_BAD_REQUEST)


class MoviesDetailApiView(APIView):
    
    def get_object(self, movie_id: int):
        return get_object_or_404(Movie, pk=movie_id)

    def get(self, request: Request, movie_id: int):
        """
        get movie
        """
        movie = self.get_object(movie_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def put(self, request: Request, movie_id: int):
        """
        edit movie \n
        In the body of the request, put a json with the format of jsons received from the server
        """
        movie = self.get_object(movie_id)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request: Request, movie_id: int):
        """
        del movie
        """
        movie = self.get_object(movie_id)
        movie.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)
