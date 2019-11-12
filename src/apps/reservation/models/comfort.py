from django.db import models as m


class Comfort(m.Model):
    COACH = 'ОБЩ'
    LOUNGE = 'ПЛЦ'
    SLEEPING = 'КУП'
    PLACE_CHOICES = [
        (COACH, "Общий"),
        (LOUNGE, "Плацкартный"),
        (SLEEPING, "Купейный"),
    ]
    place_type = m.CharField(max_length=3, choices=PLACE_CHOICES, default='')

    class Meta:
        verbose_name_plural = "place_types"
        ordering = ['pk']

    def __repr__(self):
        return f"{self.place_type}"

    def __str__(self):
        return f"{self.place_type}"
