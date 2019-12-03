from django.contrib import admin

from apps.reservation import models

admin.site.register(models.City)
admin.site.register(models.Train)
admin.site.register(models.Comfort)
