from django.contrib import admin
from .models import Genre, MoviePerson, Movie, MovieReview

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name','description')

@admin.register(MoviePerson)
class MoviePersonAdmin(admin.ModelAdmin):
    list_display = ('name','role')
    
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','poster')
    
@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    list_display = ('author','text')