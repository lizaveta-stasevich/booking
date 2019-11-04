from django.shortcuts import render, get_object_or_404
from ticket.models import Ticket
from django.views.generic import DetailView


class TicketView(DetailView):
    template_name = "ticket/ticket.html"
    model = Ticket
