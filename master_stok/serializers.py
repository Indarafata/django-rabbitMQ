from rest_framework import serializers 
from master_stok.models import MasterStock
 
 
class MasterStockSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = MasterStock
        fields = ('kode_barang',
                  'nama_barang',
                  'harga')