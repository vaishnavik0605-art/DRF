from functools import partial

from django.db.models import Model
from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404
# ----------------------------------------------------------------------------------------------------------
# # Create a StudentAPI in Django using class based views and JsonResponse
# # Create a class named StudentList that returns a list of student details as json
# # Create a class named StudentDetails that returns the details of a single student as a json dictionary
# ----------------------------------------------------------------------------------------------------------
# Create your views here.
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from app import serailizers
from app.models import Student
from app.serailizers import StudentSerializer



###API view all record
class studentList(APIView):
    def get(self,request):
        s=Student.objects.all()
        serializer_instance=StudentSerializer(s,many=True)
        # print(serializer_instance)
        return Response(serializer_instance.data)


class StudentCreate(APIView):
    def post(self,request):
        serializer_instance =StudentSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()  # save the data into model
            return Response(serializer_instance.data)  # sends the created object as response
            # if data is not valid it shoes the error message
        else:
            return Response(serializer_instance.errors)


# api view for reading a particular record
class StudentDetails(View):
    def get(self,request,i):   ## i for retrieve id(get)
        s=get_object_or_404(Student,id=i)
        serailizers_instance=StudentSerializer(s)
        return Response(serailizers_instance.data)



# API iew for updating existing record (full updation)
class StudentUpdate(View):
    def put(self,request,i):
        data=request.data
        s=get_object_or_404(Student,id=i)
        serailizer_instance=StudentSerializer(instance=s,data=data)
        if serailizer_instance.is_valid():
            serailizer_instance.save()
            return Response(serailizer_instance.data)
        else:
            return Response(serailizer_instance.errors)




#API view for update(partial) a student record
class StudentPartialUpdate(View):
    def patch(self,request,i):
        data=request.data
        s=get_object_or_404(Student,id=i)
        serailizers_instance=StudentSerializer(instance=s,data=data,partial=True)
        if serailizers_instance.is_valid():
            serailizers_instance.save()
            return Response(serailizers_instance.data)
        else:
            return Response(serailizers_instance.errors)


##api view for deleting an existing record
class StudentDelete(View):
    def delete(self,request,i):
        s=get_object_or_404(Student,id)
        s.delete()
        return Response({"message":"deleted"})





