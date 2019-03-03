from django.contrib import admin
from .models import Ticket
from .models import Operator
from .models import Tgno
from .models import Creator


# # Register your models here.
# admin.site.register(Ticket)
# admin.site.register(Operator)
# admin.site.register(Tgno)
# admin.site.register(Dpc)

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('number', 'operator')
    list_filter = ['date_open']


@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'tgno', 'email', 'phone')


@admin.register(Tgno)
class TgnoAdmin(admin.ModelAdmin):
    list_display = ('name', 'dpc')


admin.site.register(Creator)