from django.db.migrations import serializer
from django.db.models import Model
from rest_framework import serializers

from rest_framework import serializers
from app.models import Employee
#
#
# class EmployeeSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     gender_choices=(('female','FEMALE'),('male',"MALE"))
#     Name=serializers.CharField(max_length=30)
#     Emp_id=serializers.IntegerField()
#     Age=serializers.IntegerField()
#     Place=serializers.CharField(max_length=30)
#     Gender=serializers.ChoiceField(choices=gender_choices)
#     Joining_date=serializers.DateField(read_only=True)   # automatically adds current date to employee record
#     Salary=serializers.IntegerField()
#     Designation=serializers.CharField(max_length=30)
#
#     #create() is called after validation before save
#     def create(self,validated_data):
#         print(validated_data)
#         e=Employee.objects.create(**validated_data)
#         return e
# #after validation before saving
#     def update(self,instance,validated_data):
#         instance.Emp_id=validated_data.get('Emp_id',instance.Emp_id)
#         instance.Name=validated_data.get('Name',instance.Name)
#         instance.Age=validated_data.get('Age',instance.Age)
#         instance.Place=validated_data.get('Place',instance.Place)
#         instance.Gender=validated_data.get('Gender',instance.Gender)
#         instance.Salary=validated_data.get('Salary',instance.Salary)
#         instance.Designation=validated_data.get('Designation',instance.Designation)    ##these fields how we given defined in the above serialization class
#         instance.save()
#         return instance
#     ## in the case of patch this update fn is also calls in that time we only update
#     # some fields to take balance fields older values we use  instance.name etc(default value)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta: #(inner class)
        model=Employee
        fields='__all__' ## serailize all fields
        read_only_fields=['joining_date']

    def validate(self,data):
        if data['Age']<=0:
            raise serializers.ValidationError("Age should be positive")
