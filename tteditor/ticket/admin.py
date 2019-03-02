from django.contrib import admin
from .models import Ticket
from .models import Operator

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Operator)