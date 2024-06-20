from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from master_stok.models import MasterStock
from master_stok.serializers import MasterStockSerializer
from rest_framework.decorators import api_view

from django.http import HttpResponse
# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def master_stock_list(request):
    # judul = "<h1>ini master stock</h1>"
    # isi_konten = "<h3>developer</h3>"
    # output = judul + isi_konten
    # return HttpResponse(output)
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':
        tutorials = MasterStock.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = MasterStockSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
    # 'safe=False' for objects serialization
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer =  MasterStockSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = MasterStock.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 