from django.db import models

from transaction.models import Transaction
from master_customer.models import MasterCustomer
from datetime import date

class Debt(models.Model):
    # id_transaksi = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    id_customer = models.ForeignKey(MasterCustomer, on_delete=models.CASCADE)
    # tanggal_transaksi = models.DateField(default=date.today)
    # total_transaksi = models.DecimalField(max_digits=10, decimal_places=2)
    sisa_saldo = models.DecimalField(max_digits=10, decimal_places=2)
    