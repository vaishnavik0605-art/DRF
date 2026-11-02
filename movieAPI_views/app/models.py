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
