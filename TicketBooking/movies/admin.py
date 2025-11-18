from django.contrib import admin
from .models import Movies, Screen, Showtime


# Register your models here.


admin.site.register(Movies)
admin.site.register(Screen)
admin.site.register(Showtime)