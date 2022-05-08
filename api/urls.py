from django.urls import path,include
from .views import filmsList, filmDetail, getComments, deleteComment, favoritefilms, favoritefilm, FavouriteFilmListAPIView, NewsListAPIView, NewsDetailAPIView, GenreViewSet, RegisterApi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView)






urlpatterns = [
    path('token/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('filmList', filmsList),
    path('<int:filmId>', filmDetail),
    path('<int:filmId>/comments', getComments),
    path('<int:commentId>/comments/delete', deleteComment),
    path('<int:userId>/favorites', favoritefilms),
    path('<int:userId>/favorites/<int:filmId>', favoritefilm),
    path('news/', NewsListAPIView.as_view()),
    path('news/<int:newsId>', NewsDetailAPIView.as_view()),
    path("genre", GenreViewSet.as_view({'get': 'list', 'post': 'create'}), name="index"),
    path('news/<int:newsId>', NewsDetailAPIView.as_view()),
    path('register', RegisterApi.as_view()),
    #   path("completed/<int:pk>", views.completed, name="completed"),
]
