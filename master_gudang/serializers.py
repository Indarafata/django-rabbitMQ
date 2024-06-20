from rest_framework import serializers 
from master_gudang.models import MasterGudang
 
 
class MasterGudangSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = MasterGudang
        fields = ('kode_gudang',
                  'kode_barang',
                  'qty')