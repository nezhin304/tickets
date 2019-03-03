from django.shortcuts import render

from .models import Ticket
from django.db.models import Value, CharField
from django.db.models.functions import Concat


def tickets(request):
    all_tickets = Ticket.objects.all()
    return render(
        request,
        'ticket/tickets.html',
        {'tickets': all_tickets}
    )
