from django import forms as f

from reservation.models import Reservate


class SearchForm(f.ModelForm):
    class Meta:
        model = Reservate
        fields = ("dep_station", "arr_station", "place_type")
