from django.db import models

from master_gudang.models import MasterGudang
from master_stok.models import MasterStock
from master_customer.models import MasterCustomer
from datetime import date

class Transaction(models.Model):
    tanggal_transaksi = models.DateField(default=date.today)
    kode_gudang = models.ForeignKey(MasterGudang, on_delete=models.CASCADE)
    kode_barang = models.ForeignKey(MasterStock, on_delete=models.CASCADE)
    id_customer = models.ForeignKey(MasterCustomer, on_delete=models.CASCADE)
    jumlah = models.IntegerField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    # success = models.BooleanField(default=False)
    