from django.db import models
from django.contrib.auth.models import User


class Album(models.Model):
    
    name = models.CharField(max_length = 50)
    creation_date = models.DateField()
    desc = models.TextField(default="")
    
    
    def __str__(self):
       return self.name


class Photo(models.Model):
    
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    album = models.ForeignKey(Album, related_name = 'photos' , on_delete = models.CASCADE)
    date = models.DateField()
    image_url = models.URLField(max_length = 300)
    caption = models.TextField()
    
    def __str__(self):
        return str(self.id)
    
    
