from django.db import models

from master_gudang.models import MasterGudang
from master_stok.models import MasterStock
from datetime import date

class Transaction(models.Model):
    codeProduct = models.CharField(max_length=70, blank=False, default='')
    tanggal_transaksi = models.DateField(default=date.today)
    kode_transaksi = models.CharField(max_length=20, unique=True)
    kode_gudang = models.ForeignKey(MasterGudang, on_delete=models.CASCADE)
    kode_barang = models.ForeignKey(MasterStock, on_delete=models.CASCADE)
    jumlah = models.IntegerField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    # success = models.BooleanField(default=False)
    