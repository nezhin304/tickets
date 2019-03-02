from django.db import models


# Create your models here.
class Operator(models.Model):
    class Meta:
        db_table = 'operators'

    operator_name = models.CharField(max_length=100, blank=True, default=None, null=True)
    operator_tgno = models.CharField(max_length=10)
    operator_email = models.CharField(max_length=100, blank=True, default=None, null=True)
    operator_phone = models.CharField(max_length=50, blank=True, default=None, null=True)

    def __str__(self):
        return self.operator_tgno


class Ticket(models.Model):
    class Meta:
        db_table = 'tickets'

    ticket_number = models.CharField(max_length=20)
    ticket_date_open = models.DateField()
    ticket_date_close = models.DateField(blank=True, default=None, null=True)
    ticket_operator = models.ForeignKey(Operator, on_delete=models.PROTECT)

    def __str__(self):
        return self.ticket_number
