from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=30)
    director=models.CharField(max_length=30)
    language=models.CharField(max_length=30)
    year=models.IntegerField()
    runtime=models.IntegerField()
    rating=models.FloatField()

    image=models.ImageField(upload_to="movies",null=True,blank=True)


#USER MODEL DEFINITION
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    #username,password,email,first_name,last_name(these are fields that already exist in the user model here we extend the user model by custom model)
      phone=models.CharField(max_length=50,null=True)
      address=models.TextField(null=True)