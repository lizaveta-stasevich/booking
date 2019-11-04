from django.db import models as m


class Passenger(m.Model):
    surname = m.CharField(max_length=30)
    name = m.CharField(max_length=20)
    patronymic = m.CharField(max_length=30)
    phone = m.CharField(max_length=13, unique=True)
    passport_series = m.CharField(max_length=2)
    passport_number = m.CharField(max_length=6, unique=True)
    email = m.EmailField(unique=True)

    class Meta:
        verbose_name_plural = "passengers"
        ordering = ["surname"]

    def __repr__(self):
        return f"Passenger №{self.pk}:{self.surname}"

    def __str__(self):
        return f"{self.surname} ({self.pk})"
