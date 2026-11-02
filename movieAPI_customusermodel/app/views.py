### print validated data and how to retrieve single field and status

from functools import partial
from typing import reveal_type

from django.db.models import Model
from django.db.models import Q
from django.template.defaultfilters import title
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from app import serializers
from app.models import Movie
from app.serializers import UserSerializer, MovieSerializer
from rest_framework import status

# Create your views here.
#api view for creating a record
class MovieCreate(APIView):
    def post(self,request):
        serializer_instance=MovieSerializer(data=request.data) #deserialization validation+conversion

        if serializer_instance.is_valid():
            #to print data after validation
            print(serializer_instance.validated_data)
            #to take one field from data
            director=serializer_instance.validated_data['director']
            print(director)
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors)

#api view for reading all records
class MovieList(APIView):
    def get(self,request):
        m=Movie.objects.all()
        serializers_instance=MovieSerializer(m,many=True)
        return Response(serializers_instance.data,status=status.HTTP_200_OK)


#api view to read a specific record
class MovieDetails(APIView):
    def get(self,request,i):
        m=get_object_or_404(Movie,id=i)
        serializers_instance=MovieSerializer(m)
        return Response(serializers_instance.data,status=status.HTTP_200_OK)

#api view for update(fully) an existing record
class MovieUpdate(APIView):
    def put(self,request,i):
        data=request.data
        m=get_object_or_404(Movie,id=i)
        serializers_instance=MovieSerializer(instance=m,data=data)
        if serializers_instance.is_valid():
            serializers_instance.save()
            return Response(serializers_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers_instance.errors,status=status.HTTP_400_BAD_REQUEST)
#api view for update(partail) an existing record

class MoviePartialUpdate(APIView):
    def patch(self,request,i):
        data=request.data
        m=get_object_or_404(Movie,id=i)
        serializers_instance=MovieSerializer(instance=m,data=data,partial=True)
        if serializers_instance.is_valid():
            serializers_instance.save()
            return Response(serializers_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers_instance.errors,status=status.HTTP_400_BAD_REQUEST)

#api view to delete a record
class MovieDelete(APIView):
    def delete(self,request,i):
        m=get_object_or_404(Movie,id=i)
        m.delete()
        return Response({"message":"deleted"},status= status.HTTP_204_NO_CONTENT)


# class SearchAPIView(APIView):
#     def get(self,request):
#         #fetches the keyword from query parameters
#         data=request.query_params.get('search')
#         print(data)
#
#         #read all records matching with the keyword from db table(using filter)
#         m=Movie.objects.filter(Q(title__icontains=data) |
#                               Q(director__icontains=data) |
#                                Q(language__icontains=data) |
#                                Q(year__icontains=data) |
#                                Q(runtime__icontains=data) |
#                                Q(rating__icontains=data) |
#                                Q(image__icontains=data))
#         #call serializer class for serialization
#         serializer_instance=MovieSerializer(m,many=True)
#
#         #return Response to client
#         return Response(serializer_instance.data)


#-------------------------------------------------------------------------------------------#
#GENERICS FOR SEARCH
from rest_framework.filters import SearchFilter
from rest_framework import generics
class SearchAPI(generics.ListAPIView):
    queryset=Movie.objects.all()
    serializer_class =MovieSerializer
    filter_backends = [SearchFilter]
    search_fields=['title','director','language','year','runtime']



#--------------------------------------------------------------------------------------------#
#REGISTRATION
class RegistrationAPIView(APIView):
    def post(self,request):
        data=request.data
        serializer_instance=UserSerializer(data=data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


class RegisterAPIView(APIView):
    def post(self,request):
        data=request.data
        serializer_instance=UserSerializer(data=data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)