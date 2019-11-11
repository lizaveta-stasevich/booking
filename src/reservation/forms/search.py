from django import forms as f
from django.utils.translation import ugettext as _
from reservation.models import Comfort, Train, City


class SearchForm(f.ModelForm):
    dep_station = f.ModelChoiceField(queryset=City.objects.all(), label='Откуда')
    arr_station = f.ModelChoiceField(queryset=City.objects.all(), label='Куда')
    place_type = f.ModelChoiceField(queryset=City.objects.all(), required=False, label='Место')

    class Meta:
        model = Train
        fields = ("dep_station", "arr_station", "place_type")
