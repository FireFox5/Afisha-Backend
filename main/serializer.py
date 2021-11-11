from rest_framework import serializers
from .models import *
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'



class CinemaSerializer(serializers.ModelSerializer):
            class Meta:
             model = Cinema
             fields = 'id name'.split()



class GenresSerializer(serializers.ModelSerializer):
            class Meta:
             model = Genres
             fields = 'id name'.split()