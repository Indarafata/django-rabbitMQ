from rest_framework import serializers 
from debt.models import Debt
 
 
class DebtSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Debt
        fields = ('id',
                  'id_customer',
                  'sisa_saldo')