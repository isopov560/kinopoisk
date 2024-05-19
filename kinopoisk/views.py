from django.shortcuts import render
from .models import *


def movies(request):
    return render(request, "kinopoisk/movies.html")


def actors(request):
    return render(request, "kinopoisk/actors.html")


def directors(request):
    return render(request, "kinopoisk/directors.html")


def genres(request):
    return render(request, "kinopoisk/genres.html")


def movie_detail(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, "kinopoisk/movie_detail.html", {"movie": movie})


def actor_detail(request, id):
    actors = MoviePerson.objects.get(id=id)
    return render(request, "kinopoisk/actor_detail.html",{"actors": actors} )


def director_detail(request, id):
     actors = MoviePerson.objects.get(id=id)
    return render(request, "kinopoisk/actor_detail.html",{"actors": actors} )
    


def genre_detail(request, id):
    return render(request, "kinopoisk/genre_detail.html")


