from django.shortcuts import render, redirect, get_object_or_404
from movies.models import Showtime
from .models import Booking
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def select_seats(request,showtime_id):
    showtime = get_object_or_404(Showtime,id=showtime_id)
    booked = Booking.objects.filter(showtime=showtime,status='BOOKED')

    booked_seats = []

    for b in booked:
        booked_seats.extend(b.seats.split(","))

    if request.method == "POST":
        selected_seats = request.POST.get('selected_seats')
        return redirect(f"/booking/checkout/?showtime={showtime_id}&seats={selected_seats}")
    
    return render(request, "booking/select_seats.html", {
        "showtime": showtime,
        "booked_seats": booked_seats,
    })

@login_required(login_url='/accounts/login/')
def checkout(request):
    showtime_id = request.GET.get("showtime")
    seats = request.GET.get("seats")

    showtime = get_object_or_404(Showtime, id=showtime_id)

    seats_list = seats.split(",")
    total = len(seats_list) * float(showtime.ticket_price)

    return render(request, "booking/checkout.html", {
        "showtime": showtime,
        "seats": seats,
        "seats_list": seats_list,
        "total": total
    })




@login_required(login_url='/accounts/login/')
def confirm_booking(request):
    if request.method != "POST":
        return redirect("/")

    user = request.user
    if not user.is_authenticated:
        return redirect("/accounts/login/")

    showtime_id = request.POST.get("showtime")
    seats = request.POST.get("seats")

    showtime = get_object_or_404(Showtime, id=showtime_id)

    Booking.objects.create(
        user=user,
        showtime=showtime,
        seats=seats,
        status="BOOKED"
    )

    return redirect("booking:my_bookings")

@login_required(login_url='/accounts/login/')
def my_bookings(request):
    if not request.user.is_authenticated:
        return redirect("/accounts/login/")

    bookings = Booking.objects.filter(user=request.user).order_by("-booked_at")

    # Add split seat list for each booking
    for b in bookings:
        b.seat_list = b.seats.split(",")

    return render(request, "booking/my_bookings.html", {
        "bookings": bookings
    })


def confirm_booking(request):
    if request.method != "POST":
        return redirect("/")

    user = request.user
    showtime_id = request.POST.get("showtime")
    seats = request.POST.get("seats")

    showtime = get_object_or_404(Showtime, id=showtime_id)

    new_booking = Booking.objects.create(
        user=user,
        showtime=showtime,
        seats=seats,
        status="BOOKED"
    )

    return redirect(f"/booking/booking-confirmed/?booking={new_booking.booking_uuid}")


def booking_confirmed(request):
    booking_uuid = request.GET.get("booking")

    booking = Booking.objects.select_related("showtime", "showtime__movie").get(booking_uuid=booking_uuid)

    seat_list = booking.seats.split(",")

    return render(request, "booking/booking_confirmed.html", {
        "booking": booking,
        "seat_list": seat_list,
    })


