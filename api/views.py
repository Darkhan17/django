from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Film, Genre, Comment, FavoriteFilm, News
from .serializers import FilmSerializer, GenreSerializer, CommentSerializer, CommentSerializer2, FavoriteFilmSerializer, NewsSerializer




@api_view(['GET', 'POST'])
def filmsList(request):
    if request.method == 'GET':
        films = Film.objects.all()
        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'POST', 'DELETE'])
def filmDetail(request, filmId):
    try:
        film = Film.objects.get(id=filmId)
    except Film.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)

    if request.method == 'GET':
        serializer = FilmSerializer(film)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        film.delete()
        return Response({'message': 'deleted'}, status=404)


@api_view(['GET', 'POST'])
def getComments(request, filmId):
    try:
        film = Film.objects.get(id=filmId)
    except Film.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)

    if request.method == 'GET':
        serializer = CommentSerializer(film.comments.all(), many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer2(data=request.data)
        print(serializer.initial_data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['DELETE'])
def deleteComment(request, commentId):
    if request.method == "GET":
        try:
            comment = Comment.objects.get(id=commentId)
        except Comment.DoesNotExist as e:
            return Response({'message': str(e)}, status=400)

    elif request.method == 'DELETE':
        comment = Comment.objects.get(id=commentId)
        comment.delete()
        return Response({'Message: deleted'}, status=204)






class FavouriteFilmListAPIView(APIView):

    def get(self, request, userId):
        user = User.objects.get(id=userId)
        tasks = FavoriteFilm.objects.get(id=userId)
        serializer = FavoriteFilmSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FavoriteFilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FavouriteFilmDetailAPIView(APIView):

    def get(self, request, userId):
        user = User.objects.get(id=userId)
        tasks = FavoriteFilm.objects.get(id=userId)
        serializer = FavoriteFilmSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FavoriteFilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class NewsListAPIView(APIView):
    
    def get(self, request):
        tasks = News.objects.all()
        serializer = NewsSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class NewsDetailAPIView(APIView):

    def get(self, request, newsId):
        tasks = News.objects.get(id=newsId)
        serializer = NewsSerializer(tasks)
        return Response(serializer.data)




class GenreViewSet(viewsets.ModelViewSet):


    queryset = Genre.allGenres.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser]


    def create(self, request, *args, **kwargs):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)














@api_view(['GET', 'POST'])
def favoritefilms(request, userId):
    if request.method == 'GET':
        user = User.objects.get(id=userId)
        films = user.favorites.all()
        serializer = FavoriteFilmSerializer(films, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FavoriteFilmSerializer(data=request.data)
        print(serializer)
        print(serializer.is_valid())
        print(serializer.errors)
        if serializer.is_valid():
            print('valid')
            serializer.save(author=User.objects.get(id=userId))
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def favoritefilm(request, userId, filmId):
    try:
        user = User.objects.get(id=userId)
        films = user.favorites.all()
        film = films.get(id=filmId)
    except FavoriteFilm.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)

    if request.method == 'GET':
        serializer = FavoriteFilmSerializer(film)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FavoriteFilmSerializer(instance=film, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        film.delete()
        return Response({'message': 'deleted'}, status=404)


from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth.models import User
#Register API
class RegisterApi(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny,]
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })

