from django.shortcuts import render
from .serializers import HouseSerializer
from .models import House
from rest_framework import viewsets
# Create your views here.

class HouseAPIview(viewsets.ModelViewSet):

    queryset = House.objects.all()
    serializer_class = HouseSerializer
