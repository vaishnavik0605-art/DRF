"""
URL configuration for Employee_crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.syndication import views
from django.urls import path
from django.views import View

from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create',views.EmployeeCreate.as_view()),
    path('list',views.EmployeeList.as_view()),
    path('details/<int:i>',views.EmployeeDetails.as_view()),
    path('put/<int:i>',views.EmployeeUpdate.as_view()),
    path('patch/<int:i>',views.EmployeePartialUpdate.as_view()),
    path('delete/<int:i>',views.EmployeeDelete.as_view()),
]
