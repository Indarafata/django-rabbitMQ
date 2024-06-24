# transaction/tasks.py
from celery import shared_task
from master_gudang.models import MasterGudang
from debt.models import Debt
from rest_framework.parsers import JSONParser 
from transaction.serializers import TranscationSerializer
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

@shared_task
@api_view(['GET', 'POST', 'DELETE'])
def new_transaction(request):
    try:
        # transaction_data = JSONParser().parse(request)
        tutorial_serializer =  TranscationSerializer(data=request)
        tutorial_serializer.save()
        
        return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)  
    except MasterGudang.DoesNotExist:
        # pass
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@shared_task
def reduce_stock(kode_barang_transaksi, quantity):
    try:
        product = MasterGudang.objects.get(kode_barang = kode_barang_transaksi)
        product.qty -= quantity
        product.save()
    except MasterGudang.DoesNotExist:
        pass
    
@shared_task
def update_debt(customer_id, harga_total):
    try:
        debt = Debt.objects.get(id_customer = customer_id)
        debt.sisa_saldo -= harga_total
        debt.save()
    except Debt.DoesNotExist:
        pass
