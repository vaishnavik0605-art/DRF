from django.db import models

# Create your models here.
class Employee(models.Model):
    gender_choices=(('female','FEMALE'),('male',"MALE"))
    Name=models.CharField(max_length=30)
    Emp_id=models.IntegerField(unique=True)
    Age=models.IntegerField()
    Place=models.CharField(max_length=30)
    Gender=models.CharField(max_length=30,choices=gender_choices)
    Joining_date=models.DateField(auto_now_add=True)   # automatically adds current date to employee record
    Salary=models.IntegerField()
    Designation=models.CharField(max_length=30)
    image=models.ImageField(null=True,upload_to="employees",blank=True)

# class Employee(models.Model):
#     genderchoices=(('male','MALE'),('female','FEMALE'))
#     Empid=models.IntegerField(unique=True)
#     name=models.CharField(max_length=10)
#     place=models.CharField(max_length=20,null=True)
#     age=models.IntegerField()
#     gender=models.CharField(max_length=10,choices=genderchoices)
#     salary=models.IntegerField()
#     designation=models.CharField(max_length=20)
#     joiningdate=models.DateField(autonowadd=True)
#     image=models.ImageField(uploadto="employees",null=True)