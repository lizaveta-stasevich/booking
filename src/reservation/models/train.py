from math import sqrt
from django.db import models as m

from reservation.models import City


class Train(m.Model):
    COACH = 'ОБЩ'
    LOUNGE = 'ПЛЦ'
    SLEEPING = 'КУП'
    PLACE_CHOICES = [
        (COACH, "Общий"),
        (LOUNGE, "Плацкартный"),
        (SLEEPING, "Купейный"),
    ]
    num = m.CharField(max_length=3, default='', unique=True)
    dep_station = m.ForeignKey(City, on_delete=m.CASCADE, related_name='departure')
    arr_station = m.ForeignKey(City, on_delete=m.CASCADE, related_name='arrival')
    dep_time = m.TimeField()
    arr_time = m.TimeField()
    place_type = m.CharField(max_length=3, choices=PLACE_CHOICES, default='')

    class Meta:
        verbose_name_plural = "trains"
        ordering = ["dep_station"]

    def __repr__(self):
        return f"Train №{self.pk}: from {self.dep_station} to {self.arr_station}"

    def __str__(self):
        return f"{self.dep_station} - {self.arr_station}"

    def distance(self):
        degrees = sqrt(
            (self.arr_station.lat - self.dep_station.lat) ** 2 + (self.dep_station.lon - self.arr_station.lon) ** 2
        )
        return degrees * 83.0790026

    def price(self):
        classes_dict = {
            'ОБЩ': 0.018,
            'ПЛЦ': 0.03,
            'КУП': 0.05,
        }
        p = round(self.distance() * classes_dict[self.place_type])
        return p

    def get_absolute_url(self):
        return f"{reverse('train-detail', args=[str(self.pk)])}"
