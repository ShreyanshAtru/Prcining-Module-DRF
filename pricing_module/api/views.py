from xmlrpc.client import Server
from django.shortcuts import render
from .models import Price
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .serializers import PriceSerializers
from django.http.response import JsonResponse
from rest_framework import status
# Create your views here.


@api_view(['POST'])
def price_api(request):
    if request.method == 'POST':
        serializer = PriceSerializers(data=request.data)
        if serializer.is_valid():
            time = serializer.validated_data.get('TBP')
            distance = serializer.validated_data.get('DBP')
            # print(time, distance)
            if time <= 1 :
                tp = 1
            else:
                tp = 2.5
            if distance <= 10:
                dp = 1
            else:
                dp = 3
            price = (distance*dp)+(time*tp)
            serializer.save(calc_price=price)
            return Response(price, status=status.HTTP_201_CREATED) 
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
