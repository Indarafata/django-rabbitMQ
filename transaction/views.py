from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from transaction.models import Transaction
from transaction.serializers import TranscationSerializer
from rest_framework.decorators import api_view
from .tasks import reduce_stock

from django.http import HttpResponse
# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def transaction_list(request):
    # judul = "<h1>ini transaction</h1>"
    # isi_konten = "<h3>developer</h3>"
    # output = judul + isi_konten
    # return HttpResponse(output)
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':
        transaction = Transaction.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            transaction = transaction.filter(title__icontains=title)
        
        transaction_serializer = TranscationSerializer(transaction, many=True)
        return JsonResponse(transaction_serializer.data, safe=False)
    # 'safe=False' for objects serialization
    elif request.method == 'POST':
        transaction_data = JSONParser().parse(request)
        tutorial_serializer =  TranscationSerializer(data=transaction_data)
        
        # parsing data
        kode_barang = transaction_data.get('kode_barang')
        quantity = transaction_data.get('jumlah')
        
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            
            # menguangi stok gudang 
            reduce_stock.delay(kode_barang, quantity)
            
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Transaction.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 