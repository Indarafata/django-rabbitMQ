from django.db import models
from master_stok.models import MasterStock

# Create your models here.
class MasterGudang(models.Model):
    kode_gudang = models.CharField(max_length=10, primary_key=True)
    kode_barang = models.ForeignKey(MasterStock, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)