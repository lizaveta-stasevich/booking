from django.db import models as m


class Passenger(m.Model):
    surname = m.TextField()
    name = m.TextField()
    patronymic = m.TextField()
    phone = m.PositiveIntegerField(unique=True)
    passport_series = m.CharField(max_length=2)
    passport_number = m.PositiveIntegerField(unique=True)
    email = m.EmailField(unique=True)

    class Meta:
        verbose_name_plural = "passengers"
        ordering = ["surname"]

    def __repr__(self):
        return f"Passenger №{self.pk}:{self.surname}"

    def __str__(self):
        return f"{self.surname} ({self.pk})"
