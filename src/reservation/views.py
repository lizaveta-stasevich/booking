from django.shortcuts import render
from reservation.models import City


# Create your views here.
def reservation(request):
    return render(request, "reservation.html", context={
        "cities": City.objects.all(),
    })
