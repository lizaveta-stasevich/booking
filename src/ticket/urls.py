from django.urls import path
from ticket import views

urlpatterns = [
    path('<int:pk>/', views.TicketView.as_view(), name='ticket-detail'),
]
