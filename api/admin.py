from django.contrib import admin
from .models import Film, Genre, Comment, FavoriteFilm, News

# Register your models here.
admin.site.register(Film)
admin.site.register(Genre)
admin.site.register(Comment)
admin.site.register(FavoriteFilm)
admin.site.register(News)

