from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AlbumSerializer,UserSerializer,PhotoSerializer
from django.contrib.auth.models import User
from .models import *


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    
    

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer