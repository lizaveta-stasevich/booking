from django.urls import path

from . import views


urlpatterns = [
    path("", views.ReservateView.as_view(), name='reservation'),
]
