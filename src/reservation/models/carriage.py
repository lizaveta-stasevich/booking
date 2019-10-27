from django.db import models as m


class Carriage(m.Model):
    type = m.TextField(unique=True)
    amount_place = m.PositiveSmallIntegerField()
    price = m.FloatField()

    class Meta:
        verbose_name_plural = "carriages"
        ordering = ["type"]

    def __repr__(self):
        return f"Carriage №{self.pk}: {self.type}"

    def __str__(self):
        return f"{self.type} ({self.pk})"
