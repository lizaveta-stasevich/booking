from django.contrib import admin

from reservation import models

admin.site.register(models.City)
admin.site.register(models.Train)
admin.site.register(models.Passenger)
