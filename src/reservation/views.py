from django.views.generic import ListView
from reservation.forms import SearchForm
from reservation.models import Reservate


class ReservateView(ListView):
    http_method_names = ("get", "post")
    template_name = "reservation/reservation.html"
    model = Reservate

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SearchForm()
        if self.request.GET:
            context["form"] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.GET:
            f = SearchForm(self.request.GET)
            if f.is_valid():
                if f.cleaned_data["dep_station"]:
                    qs = qs.filter(dep_station=f.cleaned_data["dep_station"])
                if f.cleaned_data["arr_station"]:
                    qs = qs.filter(arr_station=f.cleaned_data["arr_station"])
                if f.cleaned_data["place_type"]:
                    qs = qs.filter(place_type=f.cleaned_data["place_type"])

        return qs
