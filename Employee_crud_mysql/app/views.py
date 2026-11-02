from calendar import error
from json import loads

from django.db.migrations import serializer
from django.db.models import Model
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

from app.models import Employee


# class EmployeeList(View):
#     def get(self,request):
#         form_data


# @method_decorator(csrf_exempt,name="dispatch")
# class EmployeeCreate(View):
#     def post(self,request):
#         form_data=(request.body)  ## fetch data from client
#         data=loads(form_data)  ## convert it into python native type
#         print(data)
#
#               ### insert into db table
#         emp = Employee.objects.create(**data)
#         emp.save()   ## save the data
#         return JsonResponse({"message":"created"})  ##return
from rest_framework.views import APIView
from rest_framework.response import Response

from app.serializers import EmployeeSerializer


class EmployeeList(APIView):
    def get(self,request):
        # e=list(Employee.objects.all().values())
        # return Response(e)

        #read all employee records from Employee table
        e=Employee.objects.all()   ## django format query set

        #converts the qs into python native using Employee serializer
        serializer_instance=EmployeeSerializer(e,many=True)
        # print(serializer_instance.data)

        return Response(serializer_instance.data)    ###to take data from serializer_instance object serializer_instance.data is used


# @method_decorator(csrf_exempt,name="dispatch")
# class EmployeeList(View):
#     def get(self,request):
#         e=list(Employee.objects.all().values())
#         print(e)
#         return JsonResponse(e,safe=False)

## apiview for reading all record
#api view for creating record
class EmployeeCreate(APIView):
    def post(self,request):
        # data=request.data    #python native data
        # e=Employee.objects.create(**data)     ## we don't need to insert every data because here we use **data
        # e.save()
        # return Response({"message":"created"})


       #validation+conversion(native to model object)
       serializer_instance=EmployeeSerializer(data=request.data)   ## class
       # print(request.data)

        #check whether the data coming from client id valid,if valid
        #save the data into model
       if serializer_instance.is_valid():
            serializer_instance.save()         #save the data into model
            return Response(serializer_instance.data) #sends the created object as response
        # if data is not valid it shoes the error message
       else:
            return Response(serializer_instance.errors)


#apiview for reading a specific employee record
class EmployeeDetails(APIView):
    def get(self,request,i):

    #reads employee record matching with id
        # e=Employee.objects.get(id=i)
        e=get_object_or_404(Employee,id=i)   # it is used when we give id that is not exist in the table exception handling


      #calls serializer class for serialization
        serializer_instance = EmployeeSerializer(e)

    # sends response back to client
        return Response(serializer_instance.data)

#apivew for deleting existing employee record
class EmployeeDelete(APIView):
    def delete(self,request,i):
        #reads record matching with id
        e=get_object_or_404(Employee,id=i)
        #deletes the record
        e.delete()
        return Response({'message':'deleted record successfully'})

#apiview for updating(full) existing employee record
class EmployeeUpdate(APIView):
    def put(self,request,i):
        #reads the record matching with id
        e=get_object_or_404(Employee,id=i)

       #fetches data coming from client
        data=request.data

      # calls employee serializer class for deserialization(v+c)
        serializer_instance=EmployeeSerializer(instance=e,data=data)  ## instance is to update the existing record without this it works as post method
        if serializer_instance.is_valid():

            #saves record
            serializer_instance.save()
            #sends response back to client
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)


#apiview for updating(patially) existing employee record

class EmployeePartialUpdate(APIView):
    def patch(self,request,i):
        #reads the record matching with id
        e=get_object_or_404(Employee,id=i)

       #fetches data coming from client
        data=request.data

      # calls employee serializer class for deserialization(v+c)
        serializer_instance=EmployeeSerializer(instance=e,data=data,partial=True)  ## instance is to update the existing record without this it works as post method
        if serializer_instance.is_valid():

            #saves record
            serializer_instance.save()
            #sends response back to client
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

