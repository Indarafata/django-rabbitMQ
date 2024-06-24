from rest_framework import serializers 
from master_customer.models import MasterCustomer
 
 
class MasterCustomerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = MasterCustomer
        fields = ('id',
                  'nama',
                  'created_at')