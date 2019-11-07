from math import sqrt
from django.db import models as m
from django.urls import reverse
from typing import Text

from reservation.models import City, Train


class Reservate(m.Model):
    COACH = 'ОБЩ'
    LOUNGE = 'ПЛЦ'
    SLEEPING = 'КУП'
    PLACE_CHOICES = [
        (COACH, "Общий"),
        (LOUNGE, "Плацкартный"),
        (SLEEPING, "Купейный"),
    ]
    dep_station = m.ForeignKey(City, on_delete=m.CASCADE, related_name="dep_st")
    arr_station = m.ForeignKey(City, on_delete=m.CASCADE, related_name="arr_st")
    place_type = m.CharField(max_length=3, choices=PLACE_CHOICES, default='')

    class Meta:
        verbose_name_plural = "reservations"
        ordering = ["pk"]

    def __repr__(self):
        return f"{self.__class__.__name__} №{self.pk}"

    def __str__(self):
        return f"Reservation № {self.pk}"

    def get_absolute_url(self) -> Text:
        return f"{reverse('reservation-detail', args=[str(self.pk)])}"

    # def distance(self):
    #     degrees = sqrt(
    #         (self.arr_station.lat - self.dep_station.lat) ** 2 + (self.dep_station.lon - self.arr_station.lon) ** 2
    #     )
    #     return degrees * 83.0790026
    #
    # def price(self):
    #     classes_dict = {
    #         'ОБЩ': 0.018,
    #         'ПЛЦ': 0.03,
    #         'КУП': 0.05,
    #     }
    #     p = round(self.distance() * classes_dict[self.place_type], 2)
    #     return p
