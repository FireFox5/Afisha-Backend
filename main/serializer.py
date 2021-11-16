from rest_framework import serializers
from .models import *


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


class MovieSerializer(serializers.ModelSerializer):
    cinema = CinemaSerializer()
    genres = GenresSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'
