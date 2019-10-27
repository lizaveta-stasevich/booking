from django.db import models as m

from reservation.models import City


class Train(m.Model):
    num = m.IntegerField(unique=True)
    dep_station = m.ForeignKey(City, on_delete=m.CASCADE, related_name='departure')
    arr_station = m.ForeignKey(City, on_delete=m.CASCADE, related_name='arrival')
    dep_time = m.TimeField()
    arr_time = m.TimeField()
    carriage_type = m.ForeignKey("Carriage", on_delete=m.CASCADE, related_name='type_of_carriage')

    class Meta:
        verbose_name_plural = "trains"
        ordering = ["dep_station"]

    def __repr__(self):
        return f"Train №{self.pk}: from {self.dep_station} to {self.arr_station}"

    def __str__(self):
        return f"{self.dep_station} - {self.arr_station} ({self.pk})"
