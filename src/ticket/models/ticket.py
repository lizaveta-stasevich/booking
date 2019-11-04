from django.db import models as m
from django.urls import reverse
from typing import Text

from reservation.models import Train, Passenger


class Ticket(m.Model):
    train_info = m.ForeignKey(Train, on_delete=m.CASCADE, related_name="tickets")
    passenger_info = m.ForeignKey(Passenger, on_delete=m.CASCADE, related_name="tickets")

    class Meta:
        verbose_name_plural = "tickets"
        ordering = ["pk"]

    def __repr__(self):
        return f"{self.__class__.__name__} №{self.pk}"

    def __str__(self):
        return f"Ticket № ({self.pk}): {self.passenger_info.surname}"

    def get_absolute_url(self) -> Text:
        return f"{reverse('ticket-detail', args=[str(self.pk)])}"
