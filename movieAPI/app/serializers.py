from unittest.result import failfast

from rest_framework import serializers
from app.models import Movie
from django.contrib.auth.models import User
from django.core.mail import send_mail
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

    def create(self,validated_data):
        u=User.objects.create_user(**validated_data)#to encrypt the password /password hashing

        #for creating a user account
        #user.objects.create_user(**validated_data)

        #for creating a superuser account
        #user.objects.create_superuser(**validated_data),automatically it will create the user as admin
        u.save()
        send_mail(
            subject="Welcome to movie app",
            message="Thank you for signing up for an account ",
            from_email="vaishnavik6677@gmail.com",
            recipient_list=[u.email],
            fail_silently=True)
        return u
