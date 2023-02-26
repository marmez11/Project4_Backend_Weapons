from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view

from .models import WeaponsTodo, Weapons_OwnerTodo
from .serializers import WeaponsTodoSerializer, WeaponsOwnerTodoSerializer

# Create your views here.
class WeaponsTodoViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = WeaponsTodo.objects.all()
    # The serializer class for serializing output
    serializer_class = WeaponsTodoSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]

class WeaponsOwnerTodoViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Weapons_OwnerTodo.objects.all()
    # The serializer class for serializing output
    serializer_class = WeaponsOwnerTodoSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]
