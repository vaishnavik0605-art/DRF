from webbrowser import register

from django.contrib import admin

from app.models import Movie,CustomUser

# Register your models here.
admin.site.register(Movie)
admin.site.register(CustomUser)