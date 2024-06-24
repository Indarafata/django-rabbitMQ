from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from debt.models import Debt
from debt.serializers import DebtSerializer
from rest_framework.decorators import api_view
# from .tasks import reduce_stock

from django.http import HttpResponse
# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def debt_list(request):
    if request.method == 'GET':
        debt = Debt.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            debt = debt.filter(title__icontains=title)
        
        debt_serializer = DebtSerializer(debt, many=True)
        return JsonResponse(debt_serializer.data, safe=False)
    # 'safe=False' for objects serialization
    elif request.method == 'POST':
        debt_data = JSONParser().parse(request)
        tutorial_serializer =  DebtSerializer(data=debt_data)
        
        # parsing data
        # kode_barang = debt_data.get('kode_barang')
        # quantity = debt_data.get('jumlah')
        
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            
            # menguangi stok gudang 
            # reduce_stock.delay(kode_barang, quantity)
            
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Debt.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 