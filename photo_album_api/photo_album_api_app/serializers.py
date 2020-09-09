from rest_framework import serializers;
from .models import *
from django.contrib.auth.models import User


class PhotoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Photo
        fields = '__all__'
        

class PhotoSerializerForNesting(serializers.ModelSerializer):
    
    class Meta:
        model = Photo
        fields = ['owner', 'image_url', 'date', 'caption']
         
         
class AlbumSerializer(serializers.ModelSerializer):
    
    photos = PhotoSerializerForNesting(many = True, read_only = True)
    
    class Meta:
        model = Album
        fields = ['photos', 'name', 'desc', 'creation_date']
        


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username']
        
