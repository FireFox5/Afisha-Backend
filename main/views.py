from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import MovieSerializer, ReviewSerializer
from main.models import Movie


# Create your views here.

@api_view(['GET'])
def print_hello(request):
    new_dic = {
        'text': 'HEllo everyone'
    }
    return Response(data=new_dic)


@api_view(['GET'])
def Movie_item_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={''})
    data = MovieSerializer(movie, many=True).data
    return Response(data=data)


@api_view(['GET'])
def Movie_list_view(request):
    movie = Movie.objects.all()
    data = MovieSerializer(movie, many=True).data
    return Response(data=data)


@api_view(['GET'])
def Reviews_list_view(request):
    review = Review.objects.all()
    data = ReviewSerializer(review, many=True).data
    return Response(data=data)


@api_view(['POST'])
def create_movie(request):
    name = request.data.get('name')
    title = request.data.get('title')
    description = request.data.get('description')
    cinema = request.data.get('cinema')
    genres = request.data.get('genres')
    Movie.objects.create(name=name)
    return Response(data={'message': 'Movie created!!!'})


@api_view(['PUT', 'DELETE'])
def delete_or_update_movie(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == 'PUT':
        movie.name = request.data.get('name', '')
        movie.save()
        return Response(data={'message': 'Movie changed'})
    elif request.method == 'DELETE':
        movie.delete()
        return Response(data={'message': 'Movie Deleted'})
