from django.db import models
from django.contrib.auth.models import User
from movies.models import Showtime
import uuid



# Create your models here.

class Booking(models.Model):
    STATUS_CHOICE = (
        ('BOOKED','Booked'),
        ('CANCELLED','Cancelled'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime,on_delete=models.CASCADE)
    seats = models.CharField(max_length=255,help_text='Comma separated seat numbers (e.g., A1,A2,A3)')
    status = models.CharField(max_length=20,choices=STATUS_CHOICE,default='BOOKED')
    booked_at = models.DateTimeField(auto_now_add=True)
    booking_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)


    def __str__(self):
        return f'{self.user.username} - {self.showtime} ({self.status})'