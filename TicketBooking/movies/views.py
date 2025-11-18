from django.shortcuts import render,get_object_or_404
from .models import Movies,Showtime

# Create your views here.

def home(request):
    movies = Movies.objects.all()
    return render(request, 'movies/home.html',{'movies':movies})

def movie_details(request,movie_id):
    movie = get_object_or_404(Movies,id=movie_id)
    showtime = Showtime.objects.filter(movie=movie).order_by('date','start_time')
    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'showtimes': showtime
    })