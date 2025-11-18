from django.urls import path
from . import views

app_name = 'booking'   # ← ADD THIS LINE


urlpatterns = [
    path('select-seats/<int:showtime_id>/', views.select_seats, name='select_seats'),
    path('checkout/', views.checkout, name='checkout'),
    path('confirm-booking/', views.confirm_booking, name='confirm_booking'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('booking-confirmed/', views.booking_confirmed, name='booking_confirmed'),


]