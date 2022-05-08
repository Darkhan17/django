from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class GenreManager(models.Manager):
    def get_queryet(self):
        return super(GenreManager, self).get_queryset()


class Genre(models.Model):
    name = models.CharField(max_length=200)
    objects = models.Manager()
    allGenres = GenreManager()
    def __str__(self):
        return f'{self.name}'



class Film(models.Model):
    name = models.CharField(max_length=300)
    img = models.CharField(max_length=1000)
    secondName = models.CharField(max_length=300)
    description = models.TextField()
    kinorium = models.FloatField()
    imbd = models.FloatField()
    critics = models.FloatField()
    country = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    worldPremiere = models.CharField(max_length=200)
    usaPremiere = models.CharField(max_length=200)
    ruPremiere = models.CharField(max_length=200)
    otherName = models.CharField(max_length=400)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return f'{self.id} : {self.name}'

class CommentManager(models.Manager):
    def get_queryet(self, given_user):
        return super(CommentManager, self).get_queryset().filter(user=given_user)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    film = models.ForeignKey(Film, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s - %s' % (self.id, self.film.name, self.user.name)


class FavoriteManager(models.Manager):
    def get_queryet(self, given_user):
        return super(FavoriteManager, self).get_queryset().filter(author=given_user)


class FavoriteFilm(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    name = models.CharField(max_length=300)
    film = models.ForeignKey(Film, related_name='film', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}'


class NewsManager(models.Manager):
    def get_queryet(self, user):
        return super(NewsManager, self).get_queryset().filter(author=user)


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news')
    name = models.CharField(max_length=300)
    text = models.CharField(max_length=1000)
    file = models.FileField(upload_to='files/%Y/%m/%d', null=True)


    def __str__(self):
        return f'{self.name}'



