from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import MovieSerializer
from main.models import Movie
# Create your views here.

@api_view(['GET'])
def print_hello(request):
    new_dic ={
        'text':'HEllo everyone'
    }
    return Response(data=new_dic)

@api_view(['GET'])
def Movie_item_view(request, id):
    movie = Movie.objects.get(id=id)
    data = MovieSerializer(movie,many=True).data
    return Response(data=data)

@api_view(['GET'])
def Movie_list_view(request):
    movie = Movie.objects.all()
    data = MovieSerializer(movie,many=True).data
    return Response(data=data)