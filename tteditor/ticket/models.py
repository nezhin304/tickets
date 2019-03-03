from django.db import models


# Create your models here.

class Tgno(models.Model):
    class Meta:
        db_table = 'operators_tgno'

    name = models.CharField(max_length=10)
    dpc = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Operator(models.Model):
    class Meta:
        db_table = 'operators'

    name = models.CharField(max_length=100, blank=True, default=None, null=True)
    tgno = models.ForeignKey(Tgno, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, blank=True, default=None, null=True)
    phone = models.CharField(max_length=50, blank=True, default=None, null=True)

    def __str__(self):

        return self.tgno.name


class Creator(models.Model):
    class Meta:
        db_table = 'creators'

    name = models.CharField(max_length=20, blank=True, default=None, null=True)

    def __str__(self):
        return self.name



class Ticket(models.Model):
    class Meta:
        db_table = 'tickets'

    number = models.CharField(max_length=20, unique=True)
    date_open = models.DateField()
    date_close = models.DateField(blank=True, default=None, null=True)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)

    def __str__(self):
        return self.number
