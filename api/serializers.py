from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import Genre, Film, Comment, FavoriteFilm, News
from django.contrib.auth.models import User


class UserSerializerСomment(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        genre = Genre.objects.create(name=validated_data['name'])
        return genre

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.save()
        return instance


class FilmSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=300, min_length=10)
    img = serializers.CharField()
    secondName = serializers.CharField(min_length=100)
    description = serializers.CharField()
    kinorium = serializers.FloatField()
    imbd = serializers.FloatField()
    critics = serializers.FloatField()
    country = serializers.CharField()
    time = serializers.CharField()
    worldPremiere = serializers.CharField(max_length=200)
    usaPremiere = serializers.CharField(max_length=200)
    ruPremiere = serializers.CharField(max_length=200)
    otherName = serializers.CharField(max_length=400)
    genres = serializers.StringRelatedField(many=True)

    def create(self, validated_data):
        film = Film.objects.create(name=validated_data['name'],
                                   img=validated_data['img'],
                                   secondName=validated_data['seconName'],
                                   description=validated_data['description'],
                                   kinorium=validated_data['kinorium'],
                                   imbd=validated_data['imbd'],
                                   critics=validated_data['critics'],
                                   country=validated_data['country'],
                                   time=validated_data['time'],
                                   worldPremiere=validated_data['worldPremiere'],
                                   usaPremiere=validated_data['usaPremiere'],
                                   ruPremiere=validated_data['ruPremiere'],
                                   otherName=validated_data['otherName'],
                                   genres=validated_data['genres'])
        return film

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializerСomment()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'film', 'body', 'date']


class CommentSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'film', 'body', 'date']


class FavoriteFilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavoriteFilm
        fields = ['id','name']
        optional_fields = ['author', ]


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = "__all__"





from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name', 'last_name')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],     password = validated_data['password']  ,first_name=validated_data['first_name'],  last_name=validated_data['last_name'])
        return user
# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
