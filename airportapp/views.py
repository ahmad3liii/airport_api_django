from django.shortcuts import render
from django.http import HttpResponse
from .models import Airport
from rest_framework.decorators import api_view
from .serializers import AirportSerializer
from rest_framework.response import Response

def airport_list(request):
    airports=Airport.objects.all()
    return render(request,'airportapp/index.html',{'airports':airports})

@api_view(['GET'])
def list_airports(request):
    food_prices=Airport.objects.all()
    serializer=AirportSerializer(food_prices,many=True)
    return Response(serializer.data)