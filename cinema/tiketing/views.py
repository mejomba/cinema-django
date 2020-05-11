from django.shortcuts import render, get_object_or_404
from tiketing.models import Movie, Cinema, Sanse

def movie_list(request):
    movies = Movie.objects.all()
    movie_count = len(movies)
    context = {
        'movie_count': movie_count,
        'movies_list' : movies
    }
    return render(request, 'tiketing/movies_list.html', context)

def cinema_list(request):
    cinemas = Cinema.objects.all()
    cinema_count = len(cinemas)
    context = {
        'cinema_count': cinema_count,
        'cinemas_list': cinemas
    }
    return render(request, 'tiketing/cinemas_list.html', context)


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {
        'movie': movie
    }
    return render(request, 'tiketing/movie_detail.html', context)


def cinema_detail(request, cinema_id):
    cinema = get_object_or_404(Cinema, pk=cinema_id)
    context = {
        'cinema': cinema
    }
    return render(request, 'tiketing/cinema_detail.html', context)