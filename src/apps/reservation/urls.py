from django.urls import path

from . import views


urlpatterns = [
    path("", views.ReservateView.as_view(), name='reservation'),
    path('<int:pk>/', views.TicketView.as_view(), name='train-detail'),
]
