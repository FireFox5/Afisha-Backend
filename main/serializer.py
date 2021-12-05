from rest_framework import serializers
from .models import Movie, Review, Cinema, Genres


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



class Movie_valid_serializator(serializers.Serializer):
    name = serializers.CharField(min_length=3,max_length=20)
    title = serializers.CharField(min_length=3,max_length=20)
    description = serializers.CharField(min_length=3,max_length=100)
    cinema_id = serializers.IntegerField()
    genres = serializers.ListField(child=serializers.IntegerField())
# class Registration_serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Registration
#         fields = '__all__'