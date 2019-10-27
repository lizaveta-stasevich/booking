from django.shortcuts import render
from reservation.models import City, Train, Passenger, Carriage


# Create your views here.
def reservation(request):
    return render(request, "reservation/reservation.html", context={
        "cities": City.objects.all(),
        "trains": Train.objects.all(),
        "passengers": Passenger.objects.all(),
        "carriages": Carriage.objects.all(),
    })
