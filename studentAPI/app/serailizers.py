from django.db.models import Model
from rest_framework import serializers
from app.models import Student

# class StudentSerializer(serializers.Serializer):
#     Name = serializers.CharField(max_length=30)
#     Age = serializers.IntegerField()
#     Course = serializers.CharField(max_length=30)
#     Mark = serializers.IntegerField()
#
#     def create(self,validated_data):
#         s=Student.objects.create(**validated_data)
#         return s


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
