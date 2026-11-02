from django.db import models

# Create your models here.

#table defintion/schema definition
class Student(models.Model):

    Name=models.CharField(max_length=30)
    Age=models.IntegerField()
    Course=models.CharField(max_length=30)
    Mark=models.IntegerField()


class Course(models.Model):
    mode_choices=(('offline','OFFLINE'),('online','ONLINE'))    ###choices=(('dbvalue'display value'))
    course_name=models.CharField(max_length=30)
    fee=models.IntegerField()
    duration=models.CharField(max_length=30)
    instructor=models.CharField(max_length=30)
    mode=models.CharField(choices=mode_choices)

