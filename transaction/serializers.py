from rest_framework import serializers 
from transaction.models import Transaction
 
 
class TranscationSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Transaction
        fields = ('id',
                  'tanggal_transaksi',
                  'jumlah',
                  'harga',
                  'id_customer',
                  'kode_barang',
                  'kode_gudang',)