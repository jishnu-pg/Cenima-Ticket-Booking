from django.db import models

# Create your models here.
# Language = (
#     ("Malayalam", 'Malayalam',),
#     ("English", 'English',),
#     ("Hindi", 'Hindi',),
#     ("Tamil", 'Tamil',),
#     ("Telungu", 'Hindi',),
#     ("Kannada", 'Kannada',),
# )

# Genre = (
#     ("Comedy", 'Comedy',),
#     ("Action", 'Action',),
#     ("Drama", 'Drama',),
#     ("Horror", 'Horror',),

# )

class Movies(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    language = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    poster_image = models.ImageField(upload_to='posters/') 

    def __str__(self):
        return self.title


class Screen(models.Model):
    name = models.CharField(max_length=200)
    total_seats = models.IntegerField()

    def __str__(self):
        return self.name

class Showtime(models.Model):
    movie = models.ForeignKey(Movies,on_delete=models.CASCADE,related_name='showtimes')
    screen = models.ForeignKey(Screen,on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    ticket_price = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return f"{self.movie.title} - {self.date} {self.start_time}"