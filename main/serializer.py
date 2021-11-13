from rest_framework import serializers
from .models import *
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
class CinemaSerializer(serializers.ModelSerializer):
            class Meta:
             model = Cinema
             fields = '__all__'
class GenresSerializer(serializers.ModelSerializer):
            class Meta:
             model = Genres
             fields = '__all__'
class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = '__all__'