from distutils.command.upload import upload
from pickle import TRUE
from tabnanny import verbose
from django.db import models

# Create your models here.

class Team(models.Model):

    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_plus_link = models.URLField(max_length=100)
    created_data = models.DateTimeField(auto_now_add=TRUE)

    def __str__(self):
        return self.first_name  #THIS IS FOR ADMIN PANNEL'S TEAMS SHOWN BASED ON FIRST_NAME
        

    class Meta:
        verbose_name = 'Teams'
        verbose_name_plural = 'Team'  #THIS IS FOR ADMIN PANNEL NAME CHANGE
    
   