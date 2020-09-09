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
        
        
    def create(self, validated_data):
        photos_data = validated_data.pop('photos')
        album=Album.objects.create(**validated_data)
        for photo_data in photos_data :
            Photo.objects.create(album=album, **photo_data)
        return album
        

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username']
        
