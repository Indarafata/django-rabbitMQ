from django.shortcuts import render


from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from master_customer.models import MasterCustomer
from master_customer.serializers import MasterCustomerSerializer
from rest_framework.decorators import api_view

from django.http import HttpResponse
# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def master_customer_list(request):
    if request.method == 'GET':
        master_customer = MasterCustomer.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            master_customer = master_customer.filter(title__icontains=title)
        
        master_customer_serializer = MasterCustomerSerializer(master_customer, many=True)
        return JsonResponse(master_customer_serializer.data, safe=False)
    # 'safe=False' for objects serialization
    elif request.method == 'POST':
        master_customer_data = JSONParser().parse(request)
        tutorial_serializer =  MasterCustomerSerializer(data=master_customer_data)
        
        # parsing data
        # kode_barang = master_customer_data.get('kode_barang')
        # quantity = master_customer_data.get('jumlah')
        
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            
            # menguangi stok gudang 
            # reduce_stock.delay(kode_barang, quantity)
            
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = MasterCustomer.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 