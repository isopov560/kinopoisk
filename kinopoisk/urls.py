from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from kinopoisk.views import *

urlpatterns = [
    path("movies/", movies, name="movies"),
    path("actors/", actors, name="actors"),
    path("directors/", directors, name="directors"),
    path("genres/", genres, name="genres"),
    path("movie_detail/<int:id>/", movie_detail, name="movie_detail"),
    path("actor_detail/<int:id>/", actor_detail, name="actor_detail"),
    path("director_detail/<int:id>/", director_detail, name="director_detail"),
    path("genre_detail/<int:id>/", genre_detail, name="genre_detail"),
]
