# transaction/tasks.py
from celery import shared_task
from master_gudang.models import MasterGudang

@shared_task
def reduce_stock(kode_barang_transaksi, quantity):
    try:
        product = MasterGudang.objects.get(kode_barang=kode_barang_transaksi)
        product.qty -= quantity
        product.save()
    except MasterGudang.DoesNotExist:
        pass
