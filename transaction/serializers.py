from rest_framework import serializers 
from transaction.models import Transaction
 
 
class TranscationSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Transaction
        fields = ('id',
                  'codeProduct',
                  'tanggal_transaksi',
                  'kode_transaksi',
                  'jumlah',
                  'harga',
                  'kode_barang',
                  'kode_gudang',)