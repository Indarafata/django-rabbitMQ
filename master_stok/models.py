from django.db import models

# Create your models here.
class MasterStock(models.Model):
    kode_barang = models.CharField(max_length=10, primary_key=True)
    nama_barang = models.CharField(max_length=255)
    harga = models.DecimalField(max_digits=10, decimal_places=2)